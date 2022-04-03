class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, n):
        self.fila.append(n)

    def denqueue(self):
        if len(self.fila) != 0:
            if self.fila[0] % 2 != 0:
                self.fila.append(self.fila[0])
                self.fila.pop(0)
            elif self.fila[0] % 2 == 0:
                self.fila.pop(0)

    def show(self):
        print(self.fila)


fila = Fila()

#lista = [401, 149, 593, 752, 701, 163, 218, 780, 608, 656, 53, 70, 994, 106, 633]
#    =   0    1    2    3    4    5    6    7    8    9   10  11  12   13    14
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tam = len(lista)

for l in lista:
    fila.enqueue(l)

for c in range(len(lista)):
    fila.denqueue()

fila.show()
