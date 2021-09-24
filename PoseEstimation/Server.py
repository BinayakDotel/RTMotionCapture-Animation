import socket               # Import socket module
import time

print("RUNNING...")
s = socket.socket()         # Create a socket object
host = "127.0.0.1" # Get local machine name
port = 8000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   time.sleep(0.5)
   c, addr = s.accept()     # Establish connection with client.
   print(f"Got connection from {addr}")
   c.send('ok'.encode('utf-8'))
   print(f"received::{s.recv(1024)}")
