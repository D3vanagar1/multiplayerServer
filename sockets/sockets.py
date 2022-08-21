
'''
Sockets are a way of connecting two nodes on a network to communicate with each other
  * one node listens on specific port at an IP address
    * other node reaches out to form a connection
'''

import socket
'''
# AF_INET: address-family ipv4
# SOCK_STREAM: coonection protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")


# connect to a server
ip = socket.gethostbyname('www.google.com')
print(ip)

# connect to google
port = 80

host_ip = socket.gethostbyname('www.google.com')
print(host_ip)

s.connect((host_ip, port))
print("socket successfully connected to google")

'''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST,PORT))
  s.listen()
  pass # use the socket without calling s.close()




