import socket
# echo_server
HOST = "127.0.0.1" # standard localhost
PORT = 65432 # port to listen to (special ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print(f"Connected by {addr}")
    while True:
      data = conn.recv(1024)
      if not data:
        break
      conn.sendall(data)
