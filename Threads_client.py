# Natália Sens Weise, BCC, 6ºsem, Sistemas Distribuídos
import socket
from threading import Thread

HOST = '127.0.0.1'    
PORT = 5000   

tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destiny = (HOST, PORT) 
tcpConnection.connect(destiny)

print('To end this connection, please type CTRL+X\n')
def message():
    message = str(input())
    while message != '\x18':
        message = str(input())
    print('Thanks for the visit, please come back soon!!\n')
    tcpConnection.close()

# print('Enter with your name:')
# name = str(input())
Thread(target=message, args=[]).start()