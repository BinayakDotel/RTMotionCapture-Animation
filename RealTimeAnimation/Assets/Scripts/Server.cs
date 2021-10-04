using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Net.Sockets;
using System.Net;
using System.Threading;
using System.Text;
using System;
using System.Diagnostics;

public class Server : MonoBehaviour
{
	Thread clientThread;
	[SerializeField] string ip = "192.168.1.1";
	[SerializeField] int port = 8000;
	[SerializeField] IPAddress ipAddress;
	[SerializeField] TcpListener listener;
	[SerializeField] TcpClient client;
	[SerializeField] string message;

	[SerializeField] Button[] serverStatus;

	[SerializeField] BodyMovement bodyMovement;

	public void Awake()
	{
		bodyMovement = BodyMovement.Instance;

		UIUpdate("Start Server", true, false);
	}
	public void EstablishCommunication()
	{

		message = "received!";
		ThreadStart threadStart = new ThreadStart(StartCommunicate);

		UIUpdate("Running...", false, false);

		clientThread = new Thread(threadStart);
		clientThread.Start();
	}
	public void StartCommunicate()
	{
		ipAddress = IPAddress.Parse(ip);

		listener = new TcpListener(IPAddress.Any, port);

		listener.Start();
		client = listener.AcceptTcpClient();

		bodyMovement.running = true;

		while (bodyMovement.running)
		{
			DataTransfer();
		}
		listener.Stop();
		StopServer();
		print("STOPPED");
	}
	public void StopServer()
	{
		if (bodyMovement.running)
		{
			message = "stop";
			bodyMovement.running = false;
		}
	}
	public void Quit()
	{
		StopServer();
		Application.Quit();
	}
	public void UIUpdate(string msg, bool show01, bool show02)
	{
		serverStatus[0].interactable = show01;
		serverStatus[0].GetComponentInChildren<Text>().text = msg;
		serverStatus[1].gameObject.SetActive(show02);
	}
	public void Update()
	{
		if (bodyMovement.running)
		{
			UIUpdate("Running...", false, true);
		}
		if(message == "stop")
		{
			UIUpdate("Start Server", true, false);
		}
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
				bodyMovement.ReceivedJoints= JsonHelper.FromJson<BodyMovement.KeyPoints>(data);
				byte[] writeBuffer = Encoding.ASCII.GetBytes(message);
				stream.Write(writeBuffer, 0, writeBuffer.Length);
			}
			catch
			{
				if (data.Equals("stop"))
				{
					message = "stop";
					bodyMovement.running = false;
				}
			}
		}
	}
}

