import socket
import time

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

connectionUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('To end this connection, please type CTRL+X\n')
print('To request for write or read, enter with "W" or "R"...\n')
actions = 0
message = str(input())
while message != '\x18' and actions <= 2:
    try:
        connectionUDP.sendto(message.encode(), dest)
        message = str(input())
    except:
        time.sleep(10)
    if message == 'R' or 'W':
        actions+=1
    if actions > 2:
        print('You time is over, the connection is ending...')
connectionUDP.close()