using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Net.Sockets;
using System.Net;
using System.Threading;
using System.Text;
using System;

public class Server : MonoBehaviour
{
	Thread clientThread;
	[SerializeField] string ip = "192.168.1.1";
	[SerializeField] int port = 8000;
	[SerializeField] IPAddress ipAddress;
	[SerializeField] TcpListener listener;
	[SerializeField] TcpClient client;
	[SerializeField] string message;

	[SerializeField] bool running;
	[SerializeField] int units;

	[SerializeField] Transform[] MovingPoints;
	[SerializeField] LineRenderer line;
	[SerializeField] Transform[] joint;

	//For smooth interpolation between keypoints
	[SerializeField] float smooth;

	//For making the movement more sensitive
	[SerializeField] Vector3[] moveSensitivity;
	[SerializeField] string currentKeypoint;

	[SerializeField] float[] rot_angle;

	[SerializeField] Vector3 HeadInitialPos;
	[SerializeField] Vector3 LeftLegInitialPos;
	[SerializeField] Vector3 RightLegInitialPos;
	[SerializeField] Vector3 HipInitialPos;

	[SerializeField] Transform Head;
	[SerializeField] Transform LeftLeg;
	[SerializeField] Transform RightLeg;
	[SerializeField] Transform Hip;


	[Serializable]
	public class Data
	{
		public string name;
		public float x;
		public float y;
		public float z;
	};
	public Data[] Joints;

	// Start is called before the first frame update
	public void Start()
	{
		EstablishCommunication();

		HeadInitialPos = MovingPoints[0].transform.position;
		LeftLegInitialPos = MovingPoints[13].transform.position;
		RightLegInitialPos = MovingPoints[14].transform.position;
	}
	public void HeadControl(Vector3 pos, int index)
	{
		print("HEAD CONTROL");
		MovingPoints[index].position = Vector3.Lerp(MovingPoints[index].position,
						new Vector3(pos.x * moveSensitivity[index].x,
									pos.y * moveSensitivity[index].y,
									pos.z * moveSensitivity[index].z), smooth);

		rot_angle[0] = Mathf.Atan((HeadInitialPos.x - pos.x) / (HeadInitialPos.y - pos.y)) * 180 / Mathf.PI;

		Quaternion currentRotationOfUpperRightLeg = MovingPoints[index].transform.rotation;
		Quaternion wantedRotationOfUpperRightLeg = Quaternion.Euler(new Vector3(0, rot_angle[0], 0));
		Head.rotation = Quaternion.RotateTowards(currentRotationOfUpperRightLeg,
			wantedRotationOfUpperRightLeg, Time.deltaTime * smooth);
	}
	public void LegControl(Vector3 pos, int index, string name, bool rotateFoot)
	{
		print("LEG CONTROL");

		MovingPoints[index].position = Vector3.Lerp(MovingPoints[index].position,
						new Vector3(pos.x * moveSensitivity[index].x,
									pos.y * moveSensitivity[index].y,
									pos.z * moveSensitivity[index].z), smooth);

		if (rotateFoot)
		{
			if (name == "LEFT_FOOT")
			{
				index = 1;
				rot_angle[index] = Mathf.Atan((LeftLegInitialPos.x - pos.x) / (LeftLegInitialPos.y - pos.y)) * 180 / Mathf.PI;
			}
			if (name == "RIGHT_FOOT")
			{
				index = 2;
				rot_angle[index] = Mathf.Atan((RightLegInitialPos.x - pos.x) / (RightLegInitialPos.y - pos.y)) * 180 / Mathf.PI;
			}

			Quaternion currentRotationOfUpperRightLeg = MovingPoints[index].transform.rotation;
			Quaternion wantedRotationOfUpperRightLeg = Quaternion.Euler(new Vector3(0, rot_angle[index], 0));

			if (name == "LEFT_FOOT")
			{
				LeftLeg.rotation = Quaternion.RotateTowards(currentRotationOfUpperRightLeg,
					wantedRotationOfUpperRightLeg, Time.deltaTime * smooth);
			}
			if (name == "RIGHT_FOOT")
			{
				RightLeg.rotation = Quaternion.RotateTowards(currentRotationOfUpperRightLeg,
					wantedRotationOfUpperRightLeg, Time.deltaTime * smooth);
			}
		}
	}
	public void HipControl(Vector3 pos, int index)
	{
		print("HIP CONTROl");
		rot_angle[3] = Mathf.Atan((HipInitialPos.x - pos.x) / (HipInitialPos.y - pos.y)) * 180 / Mathf.PI;

		Quaternion currentRotationOfUpperRightLeg = MovingPoints[index].transform.rotation;
		Quaternion wantedRotationOfUpperRightLeg = Quaternion.Euler(new Vector3(0, rot_angle[3], 0));

		LeftLeg.rotation = Quaternion.RotateTowards(currentRotationOfUpperRightLeg,
			wantedRotationOfUpperRightLeg, Time.deltaTime * smooth);
	}
	public void HandControl(Vector3 pos, int index)
	{
		print("HAND CONTROL");
		MovingPoints[index].position = Vector3.Lerp(MovingPoints[index].position,
						new Vector3(pos.x * moveSensitivity[index].x,
									pos.y * moveSensitivity[index].y,
									pos.z * moveSensitivity[index].z), smooth);
	}

	// Update is called once per frame
	void Update()
	{
		if (Joints.Length > 0)
		{
			try
			{
				int index = 0;

				foreach (Data data in Joints)
				{
					if (data.name == "NOSE_TIP")
						HeadControl(new Vector3(data.x, data.y, data.z), index);

					if (data.name == "LEFT_WRIST" || data.name == "RIGHT_WRIST")
						HandControl(new Vector3(data.x, data.y, data.z), index);

					if (data.name == "RIGHT_ANKLE" || data.name == "LEFT_ANKLE")
						LegControl(new Vector3(data.x, data.y, data.z), index, data.name, false);

					if (data.name == "LEFT_FOOT" || data.name == "RIGHT_FOOT")
						LegControl(new Vector3(data.x, data.y, data.z), index, data.name, true);

					if (data.name == "LEFT_HIP" || data.name == "RIGHT_HIP")
						HipControl(new Vector3(data.x, data.y, data.z), index);

					++index;
				}
			}
			catch
			{
				print("WAITING");
			}
		}
	}
	public void EstablishCommunication()
	{
		ThreadStart threadStart = new ThreadStart(StartCommunicate);
		clientThread = new Thread(threadStart);
		clientThread.Start();
	}
	public void StartCommunicate()
	{
		ipAddress = IPAddress.Parse(ip);

		listener = new TcpListener(IPAddress.Any, port);

		listener.Start();
		print("RUNNING...");
		client = listener.AcceptTcpClient();

		running = true;
		while (running)
		{
			DataTransfer();
			print("DATA TRANSFER");
		}
		listener.Stop();
		print("STOPPED");

		//EstablishCommunication();
	}
	public void DataTransfer()
	{
		NetworkStream stream = client.GetStream();
		byte[] buffer = new byte[client.ReceiveBufferSize];

		//receive data from host
		int byteData = stream.Read(buffer, 0, client.ReceiveBufferSize);
		string data = Encoding.UTF8.GetString(buffer, 0, byteData);

		if (data != null)
		{
			//print($"RECEIVED DATA::{data}");
			try
			{				
				Joints= JsonHelper.FromJson<Data>(data);
				byte[] writeBuffer = Encoding.ASCII.GetBytes(message);
				stream.Write(writeBuffer, 0, writeBuffer.Length);
			}
			catch
			{
				if (data.Equals("exit")) running = false;
			}
		}
	}
}

