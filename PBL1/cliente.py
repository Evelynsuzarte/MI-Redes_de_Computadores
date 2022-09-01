class Cliente:

    def __init__(self, nome, matricula, senha, status_agua, contas, id_hidrometro):

        self.nome = nome
        self.matricula = matricula
        self.senha = senha
        self.status_agua = status_agua
        self.contas = contas
        self.id_hidrometro = id_hidrometro

    def get_nome(self):
        return self.nome
    
    def get_matricula(self):
        return self.matricula

    def get_senha(self):
        return self.senha

    def get_statusAgua(self):
        return self.status_agua

    def get_contas(self):
        return self.contas
    
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

    def set_contas(self, contas):
        self.contas = contas
    
    def set_idHidrometro(self, idHidrometro):
        self.id_hidrometro = idHidrometro