import socket

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

    print ("Status do hidrômetro atualizado com sucesso!" )                                     #finalização da conexão
    tcp.close()

#servidor_recebe()
servidor_envia()




""""
FONTE DE ARQUIVO: 
https://wiki.python.org.br/SocketBasico

https://blog.4linux.com.br/socket-em-python/

https://site.sabesp.com.br/uploads/file/Folhetos/aprenda_controlar_consumo_nov2013.pdf

"""
