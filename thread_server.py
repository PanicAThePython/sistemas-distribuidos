import socket
import _thread

# definindo local do server (endereço e porta)
HOST = '127.0.0.1'     
PORT = 5000   

# estabelecendo conexão
tcpConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = (HOST, PORT) 
tcpConnection.bind(hostname) # deixa visível aos clientes
tcpConnection.listen(1) #limita o num de clientes

# guardará os avisos da sessão
warningField = []

def isConnected(con, client):
    print('Connected by', client)

    while True:
        message = connection.recv(1024) # guarda texto inserido pelo cliente
        if message.decode() == "W":
            # mostra o texto que será inserido e adiciona na lista
            print('Please, enter with your warning...\n')
            warn = connection.recv(1024)
            print('Text to be added to the WarningFields: ', warn.decode()+'\n') 
            warningField.append(warn.decode())
        elif message.decode() == "R":
            # percorre a lista, mostrando todos os avisos
            for warn in warningField:
                print(warn+'\n')
        else:
            # 'trata' possíveis equívocos de digitação
            print("This command is invalid, please enter with 'R', 'W' or CTRL+X\n")
    else:
        print('Ending connection of ', client)
        con.close()
        _thread.exit()


while True:
    connection, cliente = tcpConnection.accept()
    _thread.start_new_thread(isConnected, tuple([connection, cliente]))

tcpConnection.close()