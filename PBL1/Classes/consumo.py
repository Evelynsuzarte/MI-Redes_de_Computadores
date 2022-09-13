class Consumo:

    def __init__(self, quantidade_m3, data, hora):

        self.quantidade_m3 = quantidade_m3
        self.data = data
        self.hora = hora


    def get_quantidade_m3(self):
        return self.quantidade_m3
    
    def get_data(self):
        return self.data

    def get_hora(self):
        return self.hora


    def set_quantidade_m3(self, quantidade_m3):
        self.quantidade_m3 = quantidade_m3
    
    def set_data(self, data):
        self.data = data

    def set_hora(self, hora):
        self.hora = hora
    
    
    def somarConsumo(self, m3):
        self.quantidade_m3 = self.quantidade_m3 + m3
