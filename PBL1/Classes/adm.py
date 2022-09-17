class Adm:

    def __init__(self, nome, matricula, senha):

        self.nome = nome
        self.matricula = matricula
        self.senha = senha


    def get_nome(self):
        return self.nome
    
    def get_matricula(self):
        return self.matricula

    def get_senha(self):
        return self.senha

    def set_nome(self, nome):
        self.nome = nome
    
    def set_matricula(self, matricula):
        self.matricula = matricula

    def set_senha(self, senha):
        self.senha = senha

    def cortarAgua(self, matricula, clientes):
        while clientes != matricula:
            clientes.

