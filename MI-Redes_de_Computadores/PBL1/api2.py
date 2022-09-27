import http.server
import socket
import requests

def handle_request(request):
    """Handles the HTTP request."""

    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/index.html'

    try:
        fin = open(filename)
        content = fin.read()
        fin.close()
        response = 'HTTP/1.0 200 OK\n\n' + content

    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    return response
"""# Define socket host e port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\nHello World'
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()"""



HOST = '127.0.0.1'                                                # Capta o endereco IP do Servidor
PORT = 5000                                                     # Porta que o Servidor esta

conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #conexão TCP
conexao.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

orig = (HOST, PORT)
conexao.bind(orig)
conexao.listen(1)

while True:
    con, cliente_ade = conexao.accept()

    request = con.recv(1024).decode()
    print (request)

    #response = 'HTTP/1.0 200 OK\n\nHello World'
    response = handle_request(request)
    con.sendall(response.encode())
    con.close()
    
    print ('Finalizando conexão do cliente',cliente_ade)            #finaliza a conexão com o cliente
    conexao.close()

