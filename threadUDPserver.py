# Natália Sens Weise, BCC, 6ºsem, Sistemas Distribuídos
import socket
from threading import Thread
import time

HOST = '127.0.0.1'      
PORT = 5000            

connectionUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
connectionUDP.bind(orig)

threads = []
warnings = []

def isConnected(message, client):
    print('Connected by', client)

    isTimeOut = False
    while (not isTimeOut):
        time.sleep(10)
        warnings.append([client, message])
        isTimeOut = True
        print('Ending connection of ', client)

    if len(threads) > 0:
        threads.pop(0)
    threading()

def showWarnings():
    print('\n-----------------------------')
    print('W   A   R   N   I   N   G   S')
    for warn in warnings:
        print(warn[0],': ',warn[1])
    print('-----------------------------\n')

def threading():
    try:
        mes, cli = threads[0]
        trd = Thread(target = isConnected, args = [mes, cli])
        trd.start()
        trd.join()
    except:
        showWarnings()
        print("Waiting for new threads...\n")
        openForConnections()

def openForConnections():
    while True:
        message, client = connectionUDP.recvfrom(1024) 
        newThread =[message.decode(), client]
        threads.append(newThread)
        threading()
    
openForConnections()