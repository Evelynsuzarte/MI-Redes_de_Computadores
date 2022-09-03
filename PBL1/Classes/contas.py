class Adm:

    def __init__(self, data, valor, consumo, status_pagamento):

        self.data = data
        self.valor = valor
        self.consumo = consumo
        self.status_pagamento = status_pagamento


    def get_data(self):
        return self.data
    
    def get_valor(self):
        return self.valor

    def get_consumo(self):
        return self.consumo

    def get_status_pagamento(self):
        return self.status_pagamento

    def set_data(self, data):
        self.data = data
    
    def set_valor(self, valor):
        self.valor = valor

    def set_consumo(self, consumo):
        self.consumo = consumo

    def set_status_pagamento(self, status_pagamento):
        self.status_pagamento = status_pagamento

    def calcularValor(self,consumo)
        valorTotal = 5.00 * consumo
        return valorTotal