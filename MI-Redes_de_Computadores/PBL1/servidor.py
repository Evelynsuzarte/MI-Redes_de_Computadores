import socket
from threading import Thread
from traceback import print_tb


class Servidor():

    """def run(self):
        self.servidor_recebe()"""

    #função para receber dados ao servidor
    def servidor_recebe():
        HOST = socket.gethostbyname(socket.gethostname())               # Capta o endereco IP do Servidor
        PORT = 5000                                                     # Porta que o Servidor esta

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #conexão TCP
        orig = (HOST, PORT)
        tcp.bind(orig)
        tcp.listen(1)

        while True:
            con, cliente = tcp.accept()
            print('Conectado por',cliente)                              #sinaliza qual cliente está conectado
            while True:
                msg = con.recv(1024).decode()
                if not msg: break
                print (cliente, msg)

            print ('Finalizando conexão do cliente',cliente)            #finaliza a conexão com o cliente
            con.close()



    #função para enviar servindo como cliente
    def servidor_envia():
        HOST = socket.gethostbyname(socket.gethostname())               # Endereco IP do Servidor
        PORT = 5000                                                     # Porta que o Servidor esta
        
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # configuração TCP
        dest = (HOST, PORT)                                             # destino de envio
        tcp.connect(dest)                                         # conectando

        print(HOST)
        print(dest)

        print ("Para sair use CTRL+X \n")
        msg = input()
        tcp.send(msg.encode('utf-8'))                                   #conversão mensagem

        if msg == "ativo" or msg == "bloqueado":
            print ("Status do hidrômetro atualizado com sucesso!" )             
        else:
            print("Vazão atualizada com sucesso!")                       
        tcp.close()                                                     #finalização da conexão

#Servidor.start
Servidor.servidor_recebe()
#Servidor.servidor_envia()

