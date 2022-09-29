from threading import Thread
import time 
import socket

class Hidrometro():

    def __init__(self, id_hidrometro, matricula, consumo_atual, endereco):
        
        self.id_hidrometro = id_hidrometro      
        self.matricula = matricula              #matricula do cliente
        self.status_agua = True                 #bloqueado (False) ou ativo (True)
        self.consumo_atual = consumo_atual      #consumo do momento
        self.endereco = endereco                #endereco de registro
        self.esta_vazando = False               #vazando (true) ou nao vazando (false)


    #bloco get *****************************************************************************
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
    

    #bloco set ****************************************************************************
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
    
 
"""hidrometro = Hidrometro(1, 550010, 50, "Rua da Conceição")
hidrometro.start
hidrometro.recebeDados()"""

