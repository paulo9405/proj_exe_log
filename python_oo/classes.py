class Contador(object):
    def __init__(self):
        self.total = 0

    def zerar(self):
        self.__del__()
        return self.retornar_valor()


    def incrementar(self, valor):
        self.total += valor
        return self.retornar_valor()

    def retornar_valor(self):
        return self.total

    def __del__(self):
        self.total = 0
        return self.total