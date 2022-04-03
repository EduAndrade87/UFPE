class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

    def getLabel(self):
        return self.label

    def getNext(self):
        return self.next

    def setLabel(self, label):
        self.label = label

    def setNext(self, next):
        self.next = next


class SimplyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def adicionar(self, label):
        node = Node(label)

        if self.head == None:
            self.head = node
        elif node.getLabel() < self.head.getLabel():
            node.setNext(self.head)
            self.head = node
        else:
            aux1 = self.head
            aux2 = self.head.getNext()
            flag_insert = False
            while aux2 != None:
                if aux2.getLabel() > node.getLabel():
                    flag_insert = True
                    break
                aux1 = aux1.getNext()
                aux2 = aux2.getNext()
            if flag_insert == True:
                node.setNext(aux1.getNext())
                aux1.setNext(node)
            else:
                aux1.setNext(node)

    def mostrar(self):
        aux = self.head
        while aux != None:
            print(aux.getLabel(), end=' ')
            aux = aux.getNext()
        print()


    def reverso(self, label):
        node = Node(label)
        if self.head == None:
            self.head = node
        elif node.getLabel() > self.head.getLabel():
            node.setNext(self.head)
            self.head = node
        else:
            aux1 = self.head
            aux2 = self.head.getNext()
            flag_insert = False
            while aux2 != None:
                if aux2.getLabel() < node.getLabel():
                    flag_insert = True
                    break
                aux1 = aux1.getNext()
                aux2 = aux2.getNext()
            if flag_insert == True:
                node.setNext(aux1.getNext())
                aux1.setNext(node)
            else:
                aux1.setNext(node)

lista2=[]
lista = [55, 57, 34, 2, 17]

sll = SimplyLinkedList()

for c in lista:
    sll.adicionar(c)









