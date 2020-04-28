import os
import socket
import keyboard

address = ("127.0.0.1", 55555)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.connect(address)
s.sendall(str.encode("DHCPDISCOVER"))

while True:
    received = s.recvfrom(1024)
    messagePrefix = received[0].decode().split(";")
    print(messagePrefix)
    if messagePrefix[0] == 'DHCPOFFER':
        s.sendall(("DHCPREQUEST;" + messagePrefix[1]).encode())
        ip = messagePrefix[1]
    if(messagePrefix[0] == 'DHCPPACK'):
        print("esc to end connection")
        keyboard.wait("esc")
        s.sendall(("DHCPRELEASE;" + ip).encode())
        exit()