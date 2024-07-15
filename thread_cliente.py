import socket

HOST = '127.0.0.1'     
PORT = 5000   

tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destiny = (HOST, PORT) 
tcpConnection.connect(destiny)

print('To end this connection, please type CTRL+X\n')
message = str(input())
while message != '\x18':
    tcpConnection.send(message.encode())
    message = str(input())

print('Thanks for the visit, please come back soon!!\n')
tcpConnection.close()