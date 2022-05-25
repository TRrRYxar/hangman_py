import random
import socket
import time
serverName = '127.0.0.1'
serverPort = 8890
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((serverName, serverPort))
server_socket.listen(1)


while 1:
    connection_socket, address = server_socket.accept()
    literaNecunoscuta = "_"
    rezultatGresit = "HANGMEN"
    with open('hangmen.txt', 'r') as f:
        cuvinte = f.readlines()
    cuvant = random.choice(cuvinte)[:-1]
    nrGreseli = 0
    altcontor = 1
    litere = []
    lungimeCuvant = len(cuvant)
    contor = 0
    paraInc = "["
    paraDes = "]"
    rezGres = ''
    mesajDeTrimis = ''              # mesajul creat gol
    conditieDeOprire = 0
    while True:
        primaL = cuvant[0]                      # salvez prima si ultima litera in doua variabile
        ultimaL = cuvant[-1]
        mesajDeTrimis = mesajDeTrimis + primaL      # se adauga la mesaj prima litera
        for litera in cuvant:
            if litera.lower() in litere:
                if contor == 0:
                    contor = contor + 1         # folosesc variabila contor pentru a trece peste prima si ultima litera
                    continue
                if contor == lungimeCuvant - 1:
                    continue
                mesajDeTrimis = mesajDeTrimis + litera          # se adauga la mesaj litera care apartine
                                                            # cuvantului daca clientul o ghiceste
            else:
                if contor == 0:
                    contor = contor + 1
                    continue
                if contor == lungimeCuvant - 1:
                    continue
                mesajDeTrimis = mesajDeTrimis + literaNecunoscuta       # aici adaug in mesaj spatiile
            contor = contor + 1                                     # corespunzatoare literelor necunoscute
        mesajDeTrimis = mesajDeTrimis + ultimaL     # se adauga la mesaj ultima litera in mesaj
        contor = 0
        #time.sleep(3)
        clienta = connection_socket.recv(20).decode("utf-8")            # aici se receptioneaza litera trimisa de
        litere.append(clienta.lower())                                           # client
        altcontor = altcontor + 1
        if altcontor == 2:
            litere = []         # eliberez lista cu litere deoarece se adauga cuvantul "start" la pornirea aplicatiei
        if clienta.lower() not in cuvant.lower():
            if nrGreseli < 7:
                 mesajDeTrimis = mesajDeTrimis + '\n' + paraInc + (rezultatGresit[:nrGreseli]) + paraDes
                                                                    # aici se adauga la mesaj numarul de greseli facute
            nrGreseli += 1
            if nrGreseli == 7:
                mesajDeTrimis = 'Ai pierdut' # aici se termina jocul daca numarul de greseli este egal cu 7
                break
        else:
            mesajDeTrimis = mesajDeTrimis + '\n' + 'Litera corecta'     # se adauga "Litera corecta la mesaj
                                                    # deoarece litera nu este afisata imediat dupa momentul introducerii
        mesajDeTrimis = mesajDeTrimis.encode("utf-8")           #
        connection_socket.send(mesajDeTrimis)           # aici se trimite mesajul
                            # mesajul este format in restul codului si trimis la final
        mesajDeTrimis = ''              # aici resetez mesajul pentru a-l actualiza
        conditieDeOprire = conditieDeOprire + 1
    # if lungimeCuvant*2 == conditieDeOprire:
    #     break                                         # aici este conditia de oprire din server
    # if literaNecunoscuta not in mesajDeTrimis:           # dar am preferat sa o rulez in client
    #
    #     break
connection_socket.close()

