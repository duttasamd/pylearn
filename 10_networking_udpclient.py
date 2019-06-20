# UDP CLIENT

import socket


host = "127.0.0.1"
port = 5002

server = ("127.0.0.1", 5001)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.settimeout(2) # Timeout set to 2 seconds!

message = input("Input message:\n")

while message != "q":
    print("Sending message to server:", str(host), ":", str(port))
    s.sendto(message.encode('utf-8'), server)

    try:
        data, addr = s.recvfrom(1024)
        print("Received data:", data.decode('utf-8'))
    except socket.timeout:
        print("Didn't receive data! [Timeout]")

    message = input("-> ")

s.close()


