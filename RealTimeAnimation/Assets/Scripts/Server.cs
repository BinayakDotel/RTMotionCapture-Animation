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
	[SerializeField] int port = 9001;
	[SerializeField] IPAddress ipAddress;
	[SerializeField] TcpListener listener;
	[SerializeField] TcpClient client;
	[SerializeField] string message;
	[SerializeField] string choice = "0";
	[SerializeField] string stopMsg;

	[SerializeField] Button[] serverStatus;
	[SerializeField] GameObject[] statusPanel;

	NetworkStream stream;

	[SerializeField] BodyMovement bodyMovement;

	public void Awake()
	{
		bodyMovement = BodyMovement.Instance;

		UIUpdate("Start Server", true, false, true);
	}
	public void EstablishCommunication()
	{

		message = "received!";
		ThreadStart threadStart = new ThreadStart(StartCommunicate);

		UIUpdate("Running...", false, false, false);

		clientThread = new Thread(threadStart);
		clientThread.Start();
	}
	public void StartCommunicate()
	{
		ipAddress = IPAddress.Parse(ip);

		listener = new TcpListener(IPAddress.Any, port);

		listener.Start();
		client = listener.AcceptTcpClient();

		stream = client.GetStream();
		byte[] writeBuffer = Encoding.ASCII.GetBytes(choice);
		stream.Write(writeBuffer, 0, writeBuffer.Length);

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
			stopMsg = "stoppedServer";
			bodyMovement.running = false;
		}
	}
	public void Quit()
	{
		StopServer();
		Application.Quit();
	}
	public void UIUpdate(string msg, bool startShow, bool stopShow, bool showChoice)
	{
		if (showChoice)
		{
			print("ACTIVATE CHOICE");
			statusPanel[0].SetActive(false);
			statusPanel[1].SetActive(true);
		}
		if(!showChoice)
		{
			print("ACTIVATE SERVER PANEL");
			statusPanel[0].SetActive(true);
			statusPanel[1].SetActive(false);

			serverStatus[0].interactable = startShow;
			serverStatus[0].GetComponentInChildren<Text>().text = msg;
			serverStatus[1].gameObject.SetActive(stopShow);
		}
	}
	public void Update()
	{
		if (bodyMovement.running)
		{
			UIUpdate("Running...", false, true, false);
		}
		if(stopMsg == "stoppedServer")
		{
			UIUpdate("Start Server", true, false, true);
			stopMsg = "";
		}
	}
	public void ShowStart(string ch)
	{
		if(ch == "0")
		{
			print("WEB CAM ACTIVATED");
			choice = "0";
		}
		else if (ch == "1")
		{
			print("Video ACTIVATED");
			choice = "1";
		}
		UIUpdate("Start Server", true, false, false);
	}
	public void DataTransfer()
	{
		stream = client.GetStream();
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

