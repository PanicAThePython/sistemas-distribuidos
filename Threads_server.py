# Natália Sens Weise, BCC, 6ºsem, Sistemas Distribuídos
import socket
# import _thread
from threading import Thread

# definindo local do server (endereço e porta)
HOST = '127.0.0.1'     
PORT = 5000   


# estabelecendo conexão
tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = (HOST, PORT) 
tcpConnection.bind(hostname) # deixa visível aos clientes
tcpConnection.listen() #limita o num de clientes

# guardará os avisos da sessão
# warningField = []
threads = []

def isConnected(connection, client):
    # congela a thread
    # lock = _thread.allocate_lock()
    # lock.acquire(True, 1)

    print('Connected by', client)

    isTimeOut = False
    while not isTimeOut:
        try:
            Thread.sleep(10000)
            isTimeOut = True
        except:
            # print('preciso testar isso')
            print('Ending connection of ', client)
            connection.close()
            # _thread.exit()

def threading():
    try:
        # func = threads[0][0]
        # args = threads[0][1]
        # _thread.start_new_thread(func, args)
        threads[0].start()
        threads.remove()
        # del threads[0]
    except:
        print("Waiting for new threads...")


# _thread.TIMEOUT_MAX = 10 # definindo tempo em segundos para encerrar a thread
threading.TIMEOUT_MAX = 10
# aceitando threads
while True:
    try:
        connection, client = tcpConnection.accept()
        # newThread = [isConnected, tuple([connection, client])]
        newThread = Thread(isConnected, tuple([connection, client]))
        threads.append(newThread)
        print(threads)
        threading()
    except:
        tcpConnection.close()

