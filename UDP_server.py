import socket

HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

connectionUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = (HOST, PORT)
connectionUDP.bind(hostname)

warningField = []
onWait = []
control = False

while True:
    message, client = connectionUDP.recvfrom(1024) # guarda texto inserido pelo cliente
    actions = 0
    if not control and actions < 2:
        print("You can only do valid operations twice...")
        control = True
        while control and actions < 2:
            if message.decode() == "W":
                # mostra o texto que será inserido e adiciona na lista
                print('Please, enter with your warning...')
    
                warn = connectionUDP.recvfrom(1024)
    
                print('Text to be added to the WarningFields: ', warn[0].decode()) 
                warningField.append(str(client) + ": " + str(warn[0].decode()))
                actions+=1

            elif message.decode() == "R":
                # percorre a lista, mostrando todos os avisos
                print('\nReading Warnings...')
                for warn in warningField:
                    print(warn)
                actions+=1

            elif message.decode() == '\x18':
                control = False
                print("Closing connection...")
                connectionUDP.close()
            else:
                # 'trata' possíveis equívocos de digitação
                print("This command is invalid, please enter with 'R', 'W' or CTRL+X")

            if actions == 2:
                # se excedeu o limite, encerra conexão e começa uma nova
                control = False
                actions = 0
                print("Closing connection with", client)
                connectionUDP.close()
                connectionUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                orig = (HOST, PORT)
                connectionUDP.bind(orig)
                if len(onWait) > 0:
                    message = onWait[0][0]
                    client = onWait[0][1]
                    onWait.remove()
                else:
                    message, client = connectionUDP.recvfrom(1024)
    else:
        onWait.append([message, client])
        print('Please, wait some seconds for your time...')
   