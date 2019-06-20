# NETWORKING
# UDP Server code that receives text, performs some calculations on the text and sends the results.
import socket

host = "127.0.0.1"
port = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("Server started. Address:", host + ":" + str(port))

# c, addr = s.accept()
# print("Connection accepted. Client address :", str(addr))

while True:
    rawdata, addr = s.recvfrom(1024)

    data = rawdata.decode("utf-8")

    if not data:
        break

    print("From connected user :", str(addr), ". Data:", data)
    analysis = "Length of data: " + str(len(data)) + ". No.of words:" + str(len(data.split(' ')))

    print("Sending analysis to address :", addr)
    s.sendto(analysis.encode('utf-8'), addr)
    print("Listening ... ")

s.close()





