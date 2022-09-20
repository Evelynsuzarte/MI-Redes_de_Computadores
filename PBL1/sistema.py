from Classes.cliente import Cliente
from Classes.adm import Adm
"""from Classes.concessionaria import Concessionaria
from Classes.contas import Contas
from Classes.hidrometro import Hidrometro"""

import json

"""c = Cliente("oi",2633,"jeje")
print(c.mostrar())"""

clientesLista = []
admsLista = []
contas_abertas = []
vazamentos = []
hidrometros = []

#carregamento de dados
with open("PBL1/Dados/dados_adm.json", encoding='utf-8') as meu_json:
    adms = json.load(meu_json)

for i in adms:
    adm_atual = Adm(adms[0]['nome'],adms[0]['matricula'],adms[0]['senha'])
    admsLista.append(adm_atual)
    
print(admsLista[1].nome)

#cliente = Cliente(dados[0]['nome'],dados[0]['matricula'],dados[0]['senha'])
#print(admsLista[0])





"""for i in clientes:
    clientesLista[i] = Cliente(clientes[i]['nome'],clientes[i]['matricula'],clientes[i]['senha'], clientes[i]['id_hidrometro'])
 
for i in clientesLista:
     print(clientesLista[i])"""


"""menor = dados[0]['nome']
maior = dados[0]['matricula']"""

#print(menor)

"""cliente = dados[0]
print(cliente)"""

"""cliente = Cliente(dados[0]['nome'],dados[0]['matricula'],dados[0]['senha'])

print(cliente.mostrar())"""
"""
#___________FUNÇÕES ADM_________________

#sinalizar qnd há vazamento
def sinalizarVazamento():
    

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
"""


"""def login(matricula, senha):
    for clientes in range:
        if matricula == clientes.matricula and senha == clientes.senha:
            input()"""


