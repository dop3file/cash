import socket


sock = socket.socket()
sock.connect(("localhost", 8001))
sock.send("Hello World".encode("utf-8"))
data = sock.recv(128)
sock.close()
print(data.decode("utf-8"))