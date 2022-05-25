import socket
import time

serverName = '127.0.0.1'  # loopback address
serverPort = 8890

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

literaNecunoscuta = "_"
cont = 1
while True:
    if cont == 1:           # implementare pentru a incepe jocul la introducerea cuvantului "start"
        message = 'start'
        clientSocket.send(message.encode('utf-8'))
            # problematic si nu functioneaza fara pentru moment
    #time.sleep(3)
    mesaj = clientSocket.recv(209)          #se receptioneaza mesajul de la server
    mesaj = mesaj.decode("utf-8")       # se decodifica mesajul
    print(mesaj)                        # si se afiseaza
    print("introduceti o litera: ")
    messag = input()        # se solicita introducerea unei litere
    messag = messag.encode("utf-8")   # se codifica mesajul
    clientSocket.send(messag) # se trimite mesajul
    cont = 0
    if literaNecunoscuta not in mesaj:
        print('Felicitari cuvantul ati ghicit cuvantul!!')
        # daca cuvantul a fost ghicit se termina procesul
        break
clientSocket.close()