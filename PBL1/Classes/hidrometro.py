from threading import Thread
import random 

class Hidrometro(Thread):

    def __init__(self, nome, matricula, senha, status_agua, consumo_atual, id_hidrometro):

        self.nome = nome
        self.matricula = matricula
        self.senha = senha
        self.status_agua = status_agua
        self.consumo_atual = consumo_atual
        self.id_hidrometro = id_hidrometro

    def run(self):
        random.randrange()
        print(self.consumo_atual)

    def get_nome(self):
        return self.nome
    
    def get_matricula(self):
        return self.matricula

    def get_senha(self):
        return self.senha

    def get_statusAgua(self):
        return self.status_agua

    def get_consumo_atual(self):
        return self.consumo_atual
    
    def get_idHidrometro(self):
        return self.id_hidrometro



    def set_nome(self, nome):
        self.nome = nome
    
    def set_matricula(self, matricula):
        self.matricula = matricula

    def set_senha(self, senha):
        self.senha = senha

    def set_statusAgua(self, statusAgua):
        self.status_agua = statusAgua

    def set_consumo_atual(self, consumo_atual):
        self.consumo_atual = consumo_atual
    
    def set_idHidrometro(self, idHidrometro):
        self.id_hidrometro = idHidrometro