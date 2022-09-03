class Concessionaria:

    def __init__(self, nome, clientes, adms, contas_abertas, vazamentos):

        self.nome = nome
        self.clientes = clientes
        self.adms = adms
        self.contas_abertas = contas_abertas
        self.vazamentos = vazamentos
 
 
    def get_nome(self):
        return self.nome
    
    def get_clientes(self):
        return self.clientes

    def get_adms(self):
        return self.adms

    def get_contas_abertas(self):
        return self.contas_abertas

    def get_vazamentos(self):
        return self.vazamentos


    def set_nome(self, nome):
        self.nome = nome
    
    def set_clientes(self, clientes):
        self.clientes = clientes
    
    def set_adms(self, adms):
        self.adms = adms

    def set_contas_abertas(self, contas_abertas):
        self.contas_abertas = contas_abertas

    def set_vazamentos(self, vazamentos):
        self.vazamentos = vazamentos
    