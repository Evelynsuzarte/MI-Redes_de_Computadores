import socket 

""""
ip = socket.gethostbyname(socket.gethostname())
print(ip)
port = 5050


addr = (ip,port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 

mensagem = input("digite uma mensagem para enviar ao servidor") 
client_socket.send(mensagem) 
print ('mensagem enviada' )
client_socket.close()
"""

HOST = socket.gethostbyname(socket.gethostname())    # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print(HOST)
print(dest)

print ("Para sair use CTRL+X \n")
msg = input()
while msg != '\x18':
    tcp.send(msg.encode('utf-8'))
    msg = input()
print ('mensagem enviada' )

tcp.close()
