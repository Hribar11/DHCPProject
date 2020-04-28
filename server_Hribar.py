import socket
import random

defaultGateway = "192.168.0.1"
snMask = "255.255.255.0"
dns = "1.1.1.1"
usedIPs = []
def calc_IP():

    while(True):
        ip = random.randrange(100, 200)
        if not ip in usedIPs and ip != defaultGateway:
            break
    return "192.168.0." + str(ip)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 55555))

while True:
    received = s.recvfrom(1024)
    message = received[0].decode()
    clientAddress = received[1]
    messagePrefix = message.split(";")
    print(message)
    print(received[1])

# Message Prefixes
    if messagePrefix[0] == 'DHCPDISCOVER':
        s.sendto(str.encode("DHCPOFFER;" + calc_IP() + ";" + snMask + ";" + defaultGateway + ";" + dns), clientAddress)
    if messagePrefix[0] == "DHCPREQUEST":
        s.sendto(str.encode("DHCPPACK"), clientAddress)
        usedIPs.append(messagePrefix[1])
    if messagePrefix[0] == "DHCPRELEASE":
        usedIPs.remove(messagePrefix[1])