class Cliente:
    def __init__(self, name, years): #usa o self para interagir com os atributos
        self.name = name
        self.ra = ra

    def exibir(self):
        print(self.name, self.years)


matheus = Cliente("Matheus", 166479) #instanciando uma classe e recebendo parametros, depois se torna objeto

matheus.exibir()