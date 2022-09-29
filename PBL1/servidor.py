import socket
from threading import Thread



def run(self):
    self.servidor_recebe()

#função para receber dados ao servidor
#função que envia os dados do hidrometro
def servidor_envia(self):
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
def servidor_recebe(self):
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
#servidor_recebe()
#Servidor.start

def comecar():
    thread1 = Thread(target=servidor_envia)
    thread2 = Thread(target=servidor_recebe)

    thread1.start()
    thread2.start()

comecar()

""""
FONTE DE ARQUIVO: 
https://wiki.python.org.br/SocketBasico

https://blog.4linux.com.br/socket-em-python/

https://site.sabesp.com.br/uploads/file/Folhetos/aprenda_controlar_consumo_nov2013.pdf

"""
