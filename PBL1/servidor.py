import socket

HOST = socket.gethostbyname(socket.gethostname())               # Endereco IP do Servidor
#print(HOST)
PORT = 5000                                                     # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print ('Conectado por',cliente) 
    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg)
    print ('Finalizando conexao do cliente',cliente) 
    con.close()
"""
HOST = socket.gethostbyname(socket.gethostname())   # Endereco IP do Servidor
PORT = 5050                                         # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

#tcp.connect(dest)
tcp.bind(dest)

print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    tcp.send (msg)
    msg = input()
tcp.close()
"""
"""
https://wiki.python.org.br/SocketBasico

https://blog.4linux.com.br/socket-em-python/

https://site.sabesp.com.br/uploads/file/Folhetos/aprenda_controlar_consumo_nov2013.pdf

"""
