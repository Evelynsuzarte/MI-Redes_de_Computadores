from threading import Thread
import time 
import socket

class Hidrometro(Thread):

    def __init__(self, id_hidrometro, matricula, consumo_atual, endereco):
        
        self.id_hidrometro = id_hidrometro      
        self.matricula = matricula              #matricula do cliente
        self.status_agua = True                 #bloqueado (False) ou ativo (True)
        self.consumo_atual = consumo_atual      #consumo do momento
        self.endereco = endereco                #endereco de registro
        self.esta_vazando = False               #vazando (true) ou nao vazando (false)

    
    #bloco get
    def get_matricula(self):
        return self.matricula

    def get_statusAgua(self):
        return self.status_agua

    def get_consumo_atual(self):
        return self.consumo_atual

    def get_idHidrometro(self):
        return self.id_hidrometro

    def get_endereco(self):
        return self.endereco
    
    def get_esta_vazando(self):
        return self.esta_vazando
    

    #bloco set
    def set_matricula(self, matricula):
        self.matricula = matricula

    def set_statusAgua(self, statusAgua):
        self.status_agua = statusAgua

    def set_consumo_atual(self, consumo_atual):
        self.consumo_atual = consumo_atual
    
    def set_idHidrometro(self, idHidrometro):
        self.id_hidrometro = idHidrometro

    def set_endereco(self, endereco):
        self.endereco = endereco
    
    def set_esta_vazando(self, status):
        self.esta_vazando = status



    #função que sinaliza que há vazamento
    def vazamento(self):
        if (self.consumo_atual == 0):
            self.esta_vazando = True
        return (self.esta_vazando, self.endereco)
    

    #função que envia os dados do hidrometro
    def enviaDados(self):
        if(self.status_agua == True):
            HOST = socket.gethostbyname(socket.gethostname())    # Endereco IP do Servidor
            PORT = 5000                                          # Porta que o Servidor esta

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

        self.status_agua = msg
        print("O hidrômetro encontra-se no estado:",msg)
        
        print ('Finalizando conexao do cliente',cliente)                #finaliza a conexão com o cliente
        con.close()

 
hidrometro = Hidrometro(1, 550010, 50, "Rua da Conceição")
#hidrometro.enviaDados()
hidrometro.recebeDados()

