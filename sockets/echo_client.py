# echo_client

import socket

HOST = "127.0.0.1" # standard localhost
PORT = 65432 # port to listen to (special ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(b"Hello World")
  data = s.recv(1024)


print(f"Received {data!r}")
