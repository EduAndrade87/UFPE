class Node:
    def __init__(self, prioridade, descricao):
        self.prev = None
        self.prioridade = prioridade
        self.descricao = descricao
        self.next = None




class DoublyLinkedListPriority:
    def __init__(self):
        self.start = None
        self.end = None
        self.len = 0

    def append(self, descricao, prioridade):   #A
      if prioridade <= 10:
        if self.search(descricao) == False:
            node = Node(prioridade, descricao)
            if (self.start == None):
                #  adicionar primeiro NÓ na fila
                self.start = node
                self.end = node

            elif (self.start.prioridade < prioridade):
                #  ADD no inicio
                node.next = self.start
                self.start.prev = node
                self.start = node

            elif (self.end.prioridade >= prioridade):
                #  Add NÓ na ultima posição
                node.prev = self.end
                self.end.next = node
                self.end = node
            else:
                aux = self.start
                #  encontrar local do Nó de prioridade
                while (aux.prioridade > prioridade):
                    aux = aux.next

                #  Add NÓ
                node.next = aux
                node.prev = aux.prev
                aux.prev = node
                if (node.prev != None):
                    node.prev.next = node

            self.len += 1
            return print('tarefa adicionada com sucesso')
        else:
            return print('já tem uma atividade com essa descrição')
      else:
        print('tarefa não inserida por não ter prioridade válida')

    def dequeue(self): #C

        if self.start == self.end:
            self.end = None
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None

        self.len -= 1
        print('Tarefa executada')

    def remove(self, descricao): #D
        if self.search(descricao) == True:
            # remover uma lista com apenas 1 elemento
            if self.len == 1:
                self.start = None
            # remover o primeiro elemento da lista
            elif self.start.descricao == descricao:
                self.start = self.start.next
                self.start.prev = None
            # remover do meio ou final da lista
            else:
                aux1 = self.start
                aux2 = self.start.next
                while aux2 != None:
                    if aux2.descricao == descricao:
                        aux2 = aux2.next
                        aux1.next = aux2
                        if aux2 != None:
                            aux2.prev = aux1
                        break
                    aux1 = aux1.next
                    aux2 = aux2.next
            self.len -= 1
            print('Tarefa removida')

    def show(self): #F
        if self.start != None:
            aux = self.start
            while aux.next != None:
                print(f'Descricao: {aux.descricao}, Prioridade: {aux.prioridade}')
                aux = aux.next

            print(f'Descricao: {aux.descricao}, Prioridade: {aux.prioridade}')


    def search(self, descricao):
        aux = self.start
        self.cont = 0
        while aux != None:
            if aux.descricao == descricao:
                return True
            aux = aux.next
            self.cont += 1
        return False

    def size(self, descricao): #B
        if self.search(descricao) == True:
            print(f'serão executadas {self.cont} tarefas antes da informada')
        else:
            print('Tarefa não encontrada!')

    def empty(self):
        if self.len == 0:
            return True
        return False

    def alter(self, descricao, prioridade):
        if self.search(descricao) == True:
            self.remove(descricao)
        self.append(descricao, prioridade)

dll = DoublyLinkedListPriority()

dll.append('ListaUFPE',11)
dll.append('ListaUFPE',10)
dll.append('provaUFPE',10)
dll.append('Meditação',9)
dll.append('MétodoWimhof',9)
dll.append('ExercíciosFísicos',8)
dll.append('beberÁgua',8)
dll.append('OrganizaçãoPreventiva',7)
dll.append('ReduçãoDeAçúcar',5)
dll.append('MilagreDaManhã',4)
dll.append('Minimalismo',3)
dll.append('leitura',3)
dll.append('Jogar',1)
dll.dequeue()
dll.dequeue()
dll.show()
dll.size('Minimalismo')
dll.alter('Jogar',10)
dll.show()
