# TCP CLIENT

import socket

s = socket.socket()

host = "127.0.0.1"
port = 5000

s = socket.socket()

s.connect((host, port))
print("Connected to ", host + ":" + str(port))

message = input("Input message:\n")

while message != "q":
    print("Sending message to server...")
    s.send(message.encode('utf-8'))

    data = s.recv(1024)
    print("Received data:", data.decode('utf-8'))
    message = input("-> ")

s.close()


