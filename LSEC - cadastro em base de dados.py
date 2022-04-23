"""cadastro em base de dados

Uma empresa cadastrou vários cadastros de maneiras obscuras. Ajude-os a não virar meme implementando uma função
que resolva esse problema na base de dados deles. Considere que eles usam uma estrutura de dados baseada em uma
 linear simplesmente encadeada circular (LSEC) cujos nós armazenam RG, nome, idade, peso e altura de um grupo de
 pessoas. Considere ainda que a lista não está ordenada e pode conter pessoas repetidas (RG e/ou nome igual).
 Implemente uma função para criar uma cópia ordenada desta lista. A nova lista criada não deve conter pessoas
 repetidas ou RGs não-numéricos. (OBS: o campo que identifica unicamente uma pessoa é o RG).
 A nova lista deverá ser ordenada por ordem alfabética crescente de nomes.
 No fim, exibir a lista retornada pela função.

Entrada:

N - Tamanho da lista

X entradas na ordem RG, nome, idade, peso e altura

"""


class Node:
    def __init__(self, rg, nome, idade, peso, altura):
        self.rg = rg
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, rg, nome, idade, peso, altura):
        n = nome.lower()
        if rg.isnumeric() == True:
            if self.search(rg) == False:
                node = Node(rg, nome, idade, peso, altura)
                aux = self.head
                # inserir no inicio
                if aux == None:
                    node.next = node
                    self.head = node

                elif aux.nome >= n:
                    while aux.next != self.head:
                        aux = aux.next
                    aux.next = node
                    node.next = self.head
                    self.head = node

                else:
                    while aux.next != self.head and aux.next.nome < n:
                        aux = aux.next
                    node.next = aux.next
                    aux.next = node
                self.len += 1

    def show(self):
        aux = self.head
        print(self.head.rg, self.head.nome, self.head.idade, self.head.peso, self.head.altura)
        aux = aux.next

        while aux != self.head:
            print(aux.rg, aux.nome, aux.idade, aux.peso, aux.altura)
            aux = aux.next

    def search(self, rg):
        aux = self.head
        for i in range(self.len):
            if aux.rg == rg:
                return True
            aux = aux.next
        return False



cll = CircularLinkedList()

cll.insert('3896547', 'serginho da maciota', '85', '120', '2.1')
cll.insert('2459845', 'bruno agiota', '35', '78', '1.9')
cll.insert('4874695', 'flavinho do pneu', '16', '64', '1.7')
cll.insert('8745692', 'Alirio', '28', '65', '1.65')
cll.insert('1254664', 'chaulin matador de porco', '30', '97', '1.4')
cll.insert('3896547', 'merda', '85', '120', '2.1')
cll.insert('5763424', 'Loução da loucura', '19','85','1.7')
cll.show()




