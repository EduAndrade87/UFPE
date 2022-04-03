class Fila:
    def __init__(self):
        self.fila = []
        self.cont = []

    def enqueue(self, n):
        self.fila.append(n)

    def denqueue(self):

        if self.fila != 0:
            if self.fila[0] == self.fila[-1]:
                self.cont.append(self.fila[0])
                self.cont.append(self.fila[-1])
                self.fila.pop(0)
                self.fila.pop()


    def mostrar(self):
        print(self.fila)
        print(self.fila[-1])

    def show(self):
       if len(self.cont) != 0:
            print('VERDADE')
       else:
            print('FALSO')


fila = Fila()

p = 'AA'
#p = 'AA'

for c in p:
    fila.enqueue(c)

fila.mostrar()


for c in range(0, len(p)-1):
    fila.denqueue()
fila.show()

