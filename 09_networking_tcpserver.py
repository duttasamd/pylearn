# NETWORKING
# TCP Server code that receives text, performs some calculations on the text and sends the results.

import socket

host = "127.0.0.1"
port = 5000

s = socket.socket()
s.bind((host, port))

s.listen(1) # listen to only one connection at a time
print("Listening on: ", host + ":" + str(port))

c, addr = s.accept()
print("Connection accepted. Client address :", str(addr))

while True:
    data = c.recv(1024).decode("utf-8")

    if not data:
        break

    print("From connected user :", data)
    analysis = "Length of data: " + str(len(data)) + ". No.of words:" + str(len(data.split(' ')))

    print("Sending analysis...")
    c.send(analysis.encode('utf-8'))
    print("Listening ... ")

c.close()





