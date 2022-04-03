class Fila:
    def __init__(self):
        self.fila = []
        self.abrindoParenteses = []
        self.fechandoParenteses =[]

    def enqueue(self, n):
        self.fila.append(n)

    def denqueue(self):
        if len(self.fila) != 0:
            if self.fila[0] == '(':
                self.abrindoParenteses.append('(')
                self.fila.pop(0)
            elif self.fila[0] == ')':
                self.fechandoParenteses.append(')')
                self.fila.pop(0)
            else:
                self.fila.pop(0)

    def show(self):
        if len(self.abrindoParenteses) == len(self.fechandoParenteses):
            print('CERTO')
        else:
            if len(self.abrindoParenteses) > len(self.fechandoParenteses):
                print('ERRADO: Abre parênteses sem o fecha parênteses correspondente')
            elif len(self.abrindoParenteses) < len(self.fechandoParenteses):
                print('ERRADO: Fecha um parênteses sem ter aberto')



fila = Fila()

nome = 'A*(B+C)+D'

for c in nome:
    fila.enqueue(c)

for c in range(len(nome)):
    fila.denqueue()
fila.show()

