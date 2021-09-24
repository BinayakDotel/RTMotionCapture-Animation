using UnityEngine;
using System.Net.Sockets;
using System.Net;
using System.Threading;
using System.Text;
using System;

public class PythonClient : MonoBehaviour
{
	Thread clientThread;
	[SerializeField] string ip = "192.168.1.1";
	[SerializeField] int port = 8000;
	[SerializeField] IPAddress ipAddress;
	[SerializeField] TcpListener listener;
	[SerializeField] TcpClient client;
	[SerializeField] string message;

	[SerializeField] bool running;

	public void Start()
	{
		ThreadStart threadStart = new ThreadStart(EstablishCommunicate);
		clientThread = new Thread(threadStart);
		clientThread.Start();
	}
	public void EstablishCommunicate()
	{
		ipAddress = IPAddress.Parse(ip);
		listener = new TcpListener(IPAddress.Any, port);
		listener.Start();

		client = listener.AcceptTcpClient();

		running = true;
		while (running)
		{
			DataTransfer();
		}
		listener.Stop();
	}
	public void DataTransfer()
	{
		NetworkStream stream = client.GetStream();
		byte[] buffer = new byte[client.ReceiveBufferSize];

		//receive data from host
		int byteData = stream.Read(buffer, 0, client.ReceiveBufferSize);
		string data = Encoding.UTF8.GetString(buffer, 0, byteData);
		
		if(data != null)
		{
			print($"RECEIVED DATA::{data}");
			byte[] writeBuffer = Encoding.ASCII.GetBytes("HELLO SERVER, I AM CLIENT!!");
			stream.Write(writeBuffer, 0, writeBuffer.Length);
		}
	}
}
