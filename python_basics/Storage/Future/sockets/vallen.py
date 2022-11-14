
import socket

post = "127.0.0.1" # standard localhost
PORT = 65432 # port to listen to (special ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, post))
  s.sendall(b"not chicken nuggies steven is bad boy and he is a really really big big big big big bigbjasjdfjnvak;fjnv;kjsnefavsvfa food and belly button and i like to eat the refused food and i like to eat more food and the food is really delishiousis and i fancied the food then i shoved it in me mout")
  data = s.recv(12345678910111213141516171819202122232425262728293031323334353637383940)


print(f"Received {data!r}")
