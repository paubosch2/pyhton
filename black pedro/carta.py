class Carta:
    def __init__ (self, palo, valor): #cosntructor
        self.palo = palo
        self.valor = valor
    def __repr__ (self):
        return f"{self.valor} de {self.palo}"