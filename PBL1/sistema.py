import json
from Classes.cliente import Cliente
from Classes.adm import Adm
from Classes.hidrometro import Hidrometro
from Classes.hidrometro_serv import comecar, enviaDados
 
"""from Classes.concessionaria import Concessionaria
from Classes.contas import Contas
"""

#variaveis
clientesLista = []
admsLista = []
contas_abertasLista = []
vazamentosLista = []
hidrometrosLista = []

#carregamento de dados adm
with open("PBL1/Dados/dados_adm.json", encoding='utf-8') as meu_json:
    adms = json.load(meu_json)
count = len(adms)
for i in range(count):
    adm_atual = Adm(adms[i]['nome'],adms[i]['matricula'],adms[i]['senha'])
    admsLista.append(adm_atual)
    
#carregamento de dados hidrometro
with open("PBL1/Dados/dados_hidrometro.json", encoding='utf-8') as meu_json:
    hidrometros = json.load(meu_json)
count = len(hidrometros)
for i in range(count):
    hidrometro_atual = Hidrometro(hidrometros[i]['id_hidrometro'],hidrometros[i]['matricula'],hidrometros[i]['consumo_atual'],hidrometros[i]["endereco"])
    hidrometrosLista.append(hidrometro_atual)

#carregamento de dados clientes
with open("PBL1/Dados/dados_cliente.json", encoding='utf-8') as meu_json:
    clientes = json.load(meu_json)
count = len(clientes)
for i in range(count):
    cliente_atual = Cliente(clientes[i]['nome'],hidrometros[i]['matricula'],hidrometros[i]['senha'],hidrometros[i]["id_hidrometro"])
    clientesLista.append(cliente_atual)


print(admsLista[1].nome)
print(hidrometrosLista[1].endereco)
print(clientesLista[2].nome)




#___________FUNÇÕES ADM_________________

#sinalizar qnd há vazamento
"""def sinalizarVazamento():
   

#cortar água de uma conta em aberto passada do vencimento
def cortarAgua_cliente()

#___________FUNÇÕES CLIENTE_________________

#pagar conta em aberto
def pagarConta()

#ver histórico de contas 
def histicoContas()

#historico dos ultimos 10 consumos
def historicoConsumo()
    

#___________FUNÇÕES SISTEMA_________________

#login de adm e cliente
def login()

#logoff de adm e cliente
def logoff()

#alterar status de conta em aberto
def liberarFornecimento()

#alterar consumo atual do hidrometro
def alterarVazao()

def login(matricula, senha):
"""
comecar()

def menuHidrometro():
    print("*************** MENU HIDRÔMETRO *****************\n")
    print("---------- Vazão atual:")
    print("1. Mudar vazão atual\n2.Mudar estado")
    op = input("Digite:")
    if op == 1:
        novaVazao = input("Atualização de vazão:\nDigite a nova vazão:")
        enviaDados()
    if op == 2:
        novoEstado = input("Atualização de estado:\nDigite 'bloqueado' ou 'ativo' para mudar o estado:")