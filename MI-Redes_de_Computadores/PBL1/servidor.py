from re import I
import socket
from threading import Thread
import time
from turtle import st


HOST1 = "127.0.0.1"

#função para receber dados ao servidor------------------------------------------------------------------------------------
def servidor_recebe():
    #HOST = socket.gethostbyname(socket.gethostname())               # Capta o endereco IP do Servidor
    HOST = HOST1
    PORT_SERVER = 8000                                              # Porta que o Servidor esta

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #conexão TCP
    orig = (HOST, PORT_SERVER)      
    tcp.bind(orig)
    tcp.listen(2)                                                   

    try:
        con, cliente = tcp.accept()
        while True:
            msg = con.recv(1024).decode()
            print ("Cliente hidrômetro: ",cliente,"Consumo atual: ", msg)
            time.sleep(4)
            if not msg: break
    finally:
        print ('Finalizando conexão do cliente',cliente)            #finaliza a conexão com o cliente
        con.close()                                                 #finaliza conexão

#função para enviar servindo como cliente --------------------------------------------------------------------------------
def servidor_envia():
    #HOST = socket.gethostbyname(socket.gethostname())               # Endereco IP do Servidor
    HOST = HOST1
    PORT_CLIENT = 8009                                                     # Porta que o Servidor esta
    dest = (HOST, PORT_CLIENT)                                             # destino de envio

    while True:
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # configuração TCP                   
            tcp.connect(dest)                                               # conectando
            
            try:
                while True:
                    op = input("-------------- SISTEMA HIDRÔMETRO --------------\n1 - Bloqueio/Desbloqueio do hidrometro\n2 - Alterar vazão do hidrômetro\n0 - Sair\n--- Selecione: ")
                    if op == 1:                                     #se for opção bloquear/desbloquear
                        op2 = input("\nSelecione 1 para bloquear e 2 para desbloquear: ")
                        if op2 == 1:                                #se for para bloquear
                            msg = "bloqueado"
                            tcp.send(msg.encode('utf-8'))
                        elif op2 == 2:                              #se for para desbloquear
                            msg = "desbloqueado"
                            tcp.send(msg.encode('utf-8'))
                    elif op == 2:                                   #se for opção alterar vazão
                        novaVazao = int(input("\nDigite a nova vazão: "))
                        msg = str(novaVazao)        
                        tcp.send(msg.encode('utf-8'))
                    elif op == 0:
                        break
                    else:
                        print("Você digitou a opção errada!!")
            finally:
                print ('Finalizando conexão do cliente')            #finaliza a conexão com o cliente
                tcp.close()
        except:
            print("Conexão falhou, tentaremos conectar em 10 segundos.\nCarregando...\n")
            time.sleep(8)                                          #Tempo para uma nova tentativa

# --------------------------------  outras funções --------------------------------------------------

#função das threads
def comecar():

    thread1 = Thread(target=servidor_envia)                           #Thread para envio de dados 
    thread2 = Thread(target=servidor_recebe)                          #Thread para recebimento de dados

    thread1.start()
    time.sleep(1)     

    thread2.start()        
    time.sleep(1)                      



#------------------------------------------------

comecar()


