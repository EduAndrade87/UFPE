class Fila:
    def __init__(self):
        self.mult3 = []
        self.mult5 = []
        self.fila = []

    def enqueue(self, n):
        self.fila.append(n)

    def denqueue(self):
        if len(self.fila) != 0:
            if self.fila[0] % 3 == 0:
                self.mult3.append(self.fila[0])
            elif self.fila[0] % 5 == 0:
                self.mult5.append(self.fila[0])
            else:
                self.fila.append(self.fila[0])
        self.fila.pop(0)

    def show(self):
        print(self.mult3)
        print(self.mult5)
        print(self.fila)

fila = Fila()



for l in lista:
    fila.enqueue(l)
for c in range(len(lista)):
    fila.denqueue()
fila.show()
