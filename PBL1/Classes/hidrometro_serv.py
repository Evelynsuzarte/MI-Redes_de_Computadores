from threading import Thread
from hidrometro import Hidrometro
import json
import time 
import socket


hidrometrosLista = []
#carregamento de dados hidrometro
with open("PBL1/Dados/dados_hidrometro.json", encoding='utf-8') as meu_json:
    hidrometros = json.load(meu_json)
count = len(hidrometros)
for i in range(count):
    hidrometro_atual = Hidrometro(hidrometros[i]['id_hidrometro'],hidrometros[i]['matricula'],hidrometros[i]['consumo_atual'],hidrometros[i]["endereco"])
    hidrometrosLista.append(hidrometro_atual)


#função que envia os dados do hidrometro
def enviaDados(self):
    if(self.status_agua == True):
        HOST = socket.gethostbyname(socket.gethostname())           # Endereco IP do Servidor
        PORT = 5000                                                 # Porta que o Servidor esta

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #configuração TCP
        dest = (HOST, PORT)                                         #destino de envio
        tcp.connect(dest)                                           #conectando

        print(HOST)                                                 #print HOST
        print(dest)                                                 #print destino

        msg = str(self.consumo_atual)                               #converte para string
        while msg != '\x18':
            tcp.send(msg.encode('utf-8'))                           #conversão mensagem 
            msg = str(self.consumo_atual)
            time.sleep(2)                                           #pausa para envio de dados
            if(self.status_agua == False):
                print("Seu hidrômetro encontra-se bloqueado, entre em contato com a empresa distribuidora!!")

        print ('mensagem enviada' )                                 #finalização da conexão
        tcp.close()
    else:
        print("Seu hidrômetro encontra-se bloqueado, entre em contato com a empresa distribuidora!!")
    

#função que recebe o bloqueio e desbloqueio do hidrometro  - em 'status_agua" 
def recebeDados(self):
    HOST = socket.gethostbyname(socket.gethostname())               # Capta o endereco IP do Servidor
    PORT = 5000                                                     # Porta que o Servidor esta

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #conexão TCP
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)

    con, cliente = tcp.accept()
    print('Conectado por',cliente) 
    msg = con.recv(1024).decode()
    print (cliente, msg)

    if type(msg) == str:
        self.status_agua = msg
        print("O hidrômetro encontra-se no estado:",msg)
    if type(msg) == int:     
        self.consumo_atual = msg
        print("O hidrômetro encontra-se com vazão atual de:",msg)

    print ('Finalizando conexao do cliente',cliente)                #finaliza a conexão com o cliente
    con.close()


def comecar():
    thread1 = Thread(target=enviaDados)
    thread2 = Thread(target=recebeDados)
    

    thread1.start()
    thread2.start()
    
