# Natália Sens Weise, BCC, 6ºsem, Sistemas Distribuídos
import socket
import _thread

# definindo local do server (endereço e porta)
HOST = '127.0.0.1'     
PORT = 5000   

# estabelecendo conexão
tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = (HOST, PORT) 
tcpConnection.bind(hostname) # deixa visível aos clientes
tcpConnection.listen() #limita o num de clientes

# guardará os avisos da sessão
warningField = []

def isConnected(connection, client):
    # congela a thread
    lock = _thread.allocate_lock()
    lock.acquire(True, 1)

    print('Connected by', client)

    while lock.locked():
        try:
            print('Enter with "w" to write or "R" to read something...')
            message = connection.recv(1024) # guarda texto inserido pelo cliente
            
            if message.decode() == "W":
                # mostra o texto que será inserido e adiciona na lista
                print('Please, enter with your warning...')
                warn = connection.recv(1024)

                print('Text to be added to the WarningFields: ', warn.decode()) 
                warningField.append(warn.decode())

            elif message.decode() == "R":
                # percorre a lista, mostrando todos os avisos
                print('Reading warning field...')
                for warn in warningField:
                    print(warn)

            elif message.decode() == '':
                # descongela a thread, liberando pra próxima
                lock.release() 
                print('Ending connection of ', client)
                connection.close()
                # _thread.exit()
            else:
                # 'trata' possíveis equívocos de digitação
                print("This command is invalid, please enter with 'R', 'W' or CTRL+X")
        except:
            print('preciso testar isso')
            print('Ending connection of ', client)
            connection.close()
            _thread.exit()


_thread.TIMEOUT_MAX = 10 # definindo tempo em segundos para encerrar a thread

# aceitando threads
while True:
    try:
        connection, client = tcpConnection.accept()
        _thread.start_new_thread(isConnected, tuple([connection, client]))
    except:
        tcpConnection.close()

