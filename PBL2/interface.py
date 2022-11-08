from nevoa import manipularBanco

def interfaceCliente():
    print("\n---------------  CLIENTE HIDRÔMETRO ---------------\nSeja bem vindo(a)! Selecione a opção correspondente:\n")
    print("1. Visualizar histórico do hidrômetro")
    print("2. Visualizar consumo atual")
    print("3. Pagar conta")
    print("4. Valor conta atual")
    print("0. Sair\n")
    op = int(input(">>>>>> Selecione: "))

    if op == 1:
        print("------------ Visualizar histórico do hidrômetro ------------")
        id = int(input(">>>>>> Digite o ID do hidrômetro: "))
        manipularBanco.exibirHistorico(id)
    elif op == 2:
        print("------------ Visualizar consumo atual ------------")
        id = int(input(">>>>>> Digite o ID do hidrômetro: "))
        manipularBanco.consultarConsumo(id)
    elif op == 3:
        print("------------ Visualizar hidrômetro selecionado ------------")
    elif op == 4:
        print("------------ Valor conta atual ------------")
    elif op == 0:
        print("Saindo...")


def interfaceAdm():
    print("---------------  ADMINISTRADOR ---------------\nSeja bem vindo(a)! Selecione a opção correspondente:\n")
    print("1. Hidrômetros com contas em débito")
    print("2. Visualização dos n hidrômetros com maiores gastos")
    print("3. Visualizar hidrômetro selecionado")
    print("4. Bloqueio por valor de teto de gastos")
    print("5. Visualizar hidrômetros com vazamento")
    print("0. Sair\n")
    op = int(input(">>>>>> Selecione: "))

    if op == 1:
        print("------------ Hidrômetros em aberto ------------")
    elif op == 2:
        print("------------ Visualização dos n hidrômetros ------------")
    elif op == 3:
        print("------------ Visualizar hidrômetro selecionado ------------")
    elif op == 4:
        print("------------ Bloqueio por valor de teto de gastos ------------")
    elif op == 5:
        print("------------ Visualizar hidrômetros com vazamento ------------")
    elif op == 0:
        print("Saindo...")

def main():
    while(True):
        perfil = int(input("------------- Você é?\n1.Cliente\n2.Administrador\n>>>>>> Selecione: "))
        if perfil == 1:
            interfaceCliente()
        elif perfil == 2:
            interfaceAdm()

main()