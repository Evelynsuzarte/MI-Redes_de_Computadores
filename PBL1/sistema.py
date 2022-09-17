from Classes
from PBL1.Classes.cliente import Cliente
from PBL1.Classes.concessionaria import Concessionaria
from PBL1.Classes.consumo import Comsumo
from PBL1.Classes.contas import Contas
from PBL1.Classes.hidrometro import Hidrometro

clientes = []
adms = []
contas_abertas = []
vazamentos = []
hidrometros = []

def cadastrarCliente():
    nome = input()
    matricula = input()
    senha = input()
    id_hidrometro = input()

    cliente_novo = Cliente(nome,matricula,senha,True,[],[],id_hidrometro)

    print(cliente_novo)



"""def login(matricula, senha):
    for clientes in range:
        if matricula == clientes.matricula and senha == clientes.senha:
            input()"""




cadastrarCliente()
