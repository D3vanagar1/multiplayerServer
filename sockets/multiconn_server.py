import sys
import socket
import selectors
import types


sel = selectors.DefaultSelector()

host, port = ("127.0.0.1", 65432)
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host,port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)