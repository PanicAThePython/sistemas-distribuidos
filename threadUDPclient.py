# Natália Sens Weise, BCC, 6ºsem, Sistemas Distribuídos
import cmd
import socket
import time

HOST = '127.0.0.1'
PORT = 5000            
connectionUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('To end this connection, please type CTRL+X\n')

message = str(input())
while True:
    try:
        connectionUDP.sendto(message.encode(), dest)
        message = str(input())
        if message == '\x18':
            connectionUDP.close()
    except :
        connectionUDP.close()