import socket
import time
from threading import Thread
from hidrometro import Hidrometro


hidrometro = Hidrometro(1, 550010, 50, "Avenida do Alfabeto, 78, Tombinha")
HOST1 = "127.0.0.1"


# --------------------------------  funções de conexão --------------------------------------------------

#função que envia os dados de consumo do hidrometro -----------------------------------------------------
def enviaDados():
    try:
        #HOST = socket.gethostbyname(socket.gethostname())           # Endereco IP do Servidor
        HOST = HOST1
        PORT_CLIENTE = 8000                                         # Porta que o Servidor esta

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #configuração TCP
        dest = (HOST, PORT_CLIENTE)                                 #destino de envio
        tcp.connect(dest)                                           #conectando ao destino

        while True:
            if(hidrometro.get_statusAgua() == True):                        #se não tiver bloqueado

                print(HOST)                                                 #print HOST
                print(dest)                                                 #print destino

                msg = str(hidrometro.get_consumo_atual())                   #converte para string
                while msg != '\x18':
                    tcp.send(msg.encode('utf-8'))                           #codificação da mensagem 
                    msg = str(hidrometro.get_consumo_atual())               #a msg é o consumo atual
                    
                    dado = int(msg)
                    hidrometro.atualizarHistorico(dado)
                    time.sleep(4)                                           #pausa para envio de dados

                    
                    if(hidrometro.get_statusAgua() == False):               #se caso bloquear durante o processo
                        break
                    if not msg: break

                print ('mensagem enviada' )                                 #finalização da conexão
                tcp.close()
            else:
                print("Seu hidrômetro encontra-se bloqueado, entre em contato com a empresa distribuidora!!")
                time.sleep(4)   
    except:
        print("Falha no envio de dados!")                                            

#função que recebe o bloqueio e desbloqueio do hidrometro  - em 'status_agua" --------------------------------------
def recebeDados():
    #HOST = socket.gethostbyname(socket.gethostname())               # Capta o endereco IP do Servidor
    HOST = HOST1
    PORT_SERVER = 5000                                              # Porta que o Servidor está
    
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #conexão TCP
    orig = (HOST, PORT_SERVER)
    tcp.bind(orig)
    tcp.listen(2)

    while True:
        print("Carregando....")
        con, cliente = tcp.accept()
        print('Conectado por: ',cliente)
        msg = con.recv(1024).decode()                                   #decodificação da mensagem
        print (cliente, msg)                                                

        try:
            #ifs para controlar bloqueio do hidrometro
            print(msg)
            if (msg == 'desbloqueado'):                                        
                hidrometro.atualizarStatus("desbloqueado")                     #atualização de novo status
                print ("Status atual do hidrômetro: desbloqueado")
            elif (msg == 'bloqueado'):
                hidrometro.atualizarStatus("bloqueado")
                print ("Status atual do hidrômetro: bloqueado")
            elif (msg == 'historico'):
                listaHistorico = hidrometro.get_historico()
                print("HISTÓRICO DAS 10 ÚLTIMAS VAZÕES:\n")
                print(listaHistorico)
                """for i in range (len(listaHistorico)):
                    print(listaHistorico[i])"""
            elif (msg == 'consumo total'):
                print("Consumo total do período: ",hidrometro.get_consumo_total())
                print("\n")
            #else para caso seja um número controla a vazao
            else:
                vazao = int(msg)
                if vazao > 0:                           
                    hidrometro.set_consumo_atual(vazao)                 #atualização de nova vazãos
                    print ("Atualizada a vazão do hidrometro:", vazao, "l/m³")
                elif vazao == 0:
                    hidrometro.set_consumo_atual(vazao)
                    hidrometro.set_esta_vazando(True)
                    print ("Atualizada a vazão do hidrometro:", vazao, "l/m³. HIDRÔMETRO COM VAZAMENTO")
        except:
            print ("Não conectado ao cliente!!")    
        finally:
            print ('Finalizando conexao do cliente',cliente)                #finaliza a conexão com o cliente
            con.close()


# --------------------------------  outras funções --------------------------------------------------

#função para fazer a verificação de vazamento do hidrometro
def verificacaoVazamento():
    while True:
        if (hidrometro.vazamento() == True):                                #Caso tenha vazamento - alerta de vazamento
            print("STATUS: !!! ENCONTRADO VAZAMENTO NA REDE !!! \nHIDRÔMETRO: ",hidrometro.get_matricula(), "no endereço:", hidrometro.get_endereco())                  
        else: 
            print("STATUS: Hidrômetro sem vazamentos!!");          #Sem vazamento
        time.sleep(15)                                                      #Tempo de verificação

#função para fazer a atualização do consumo total
def somaConsumoTotal():
    while True:
        if hidrometro.get_statusAgua() == True:                             #verificação de bloqueio de hidrômetro
            consumo_aux = hidrometro.get_consumo_total() + hidrometro.get_consumo_atual()
            hidrometro.set_consumo_total(consumo_aux)
            time.sleep(4)

#função das threads
def comecar():

    thread1 = Thread(target=enviaDados)                           #Thread para envio de dados 
    thread2 = Thread(target=recebeDados)                          #Thread para recebimento de dados
    thread3 = Thread(target=verificacaoVazamento)                 #Thread para verificação de vazamento
    thread4 = Thread(target=somaConsumoTotal)                     #Thread para atualização de consumo total

    thread1.start()                               
    thread2.start()                             
    thread3.start()      
    thread4.start()   


#------------------------------------------------

comecar()

