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

	[SerializeField] BodyMovement bm;

	public void Awake()
	{
		bm = BodyMovement.Instance;

		UIUpdate("Start Server", true);
	}
	public void EstablishCommunication()
	{
		Process process = new Process();
		process.StartInfo.FileName = "cmd.exe";
		process.StartInfo.CreateNoWindow = true;
		process.StartInfo.RedirectStandardInput = true;
		process.StartInfo.UseShellExecute = false;
		process.StartInfo.RedirectStandardOutput = true;
		process.Start();

		message = "received!";
		ThreadStart threadStart = new ThreadStart(StartCommunicate);

		UIUpdate("running...", false);

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
		bm.running = true;

		while (bm.running)
		{
			DataTransfer();
			print("DATA TRANSFER");
		}
		listener.Stop();
		StopServer();
		print("STOPPED");
	}
	public void StopServer()
	{
		if (bm.running)
		{
			message = "stop";
			bm.running = false;
		}
	}
	public void Quit()
	{
		StopServer();
		Application.Quit();
	}
	public void UIUpdate(string msg, bool show)
	{
		serverStatus[0].interactable = show;
		serverStatus[0].GetComponentInChildren<Text>().text = msg;
		serverStatus[1].gameObject.SetActive(!show);
	}
	public void Update()
	{
		if(message == "stop")
		{
			UIUpdate("Start Server", true);
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
				bm.ReceivedJoints= JsonHelper.FromJson<BodyMovement.KeyPoints>(data);
				byte[] writeBuffer = Encoding.ASCII.GetBytes(message);
				stream.Write(writeBuffer, 0, writeBuffer.Length);
			}
			catch
			{
				if (data.Equals("stop"))
				{
					message = "stop";
					bm.running = false;
				}
			}
		}
	}
}

