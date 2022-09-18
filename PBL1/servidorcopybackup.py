import socket

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
            msg = con.recv(1024)
            if not msg: break
            print (cliente, msg)

        print ('Finalizando conexao do cliente',cliente)            #finaliza a conexão com o cliente
        con.close()

def servidor_envia():
    HOST = socket.gethostbyname(socket.gethostname())               # Endereco IP do Servidor
    PORT = 5000                                                      # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #configuração TCP
    dest = (HOST, PORT)     #destino de envio
    tcp.connect(dest)       #conectando

    print(HOST)
    print(dest)

    print ("Para sair use CTRL+X \n")
    msg = input()
    while msg != '\x18':
        tcp.send(msg.encode('utf-8'))   #conversão mensagem
        msg = input()
    print ('mensagem enviada' )

    tcp.close()


""""

FONTE DE ARQUIVO: 
https://wiki.python.org.br/SocketBasico

https://blog.4linux.com.br/socket-em-python/

https://site.sabesp.com.br/uploads/file/Folhetos/aprenda_controlar_consumo_nov2013.pdf

"""
