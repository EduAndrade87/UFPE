#Produto
class Produto:
  #Construtor
  def __init__(self,codigo,descricao,preco,estoque):
    self.codigo = codigo
    self.descricao = descricao
    self.preco = preco
    self.estoque = estoque

  #Getters
  def getCodigo(self):
    return self.codigo

  def getDescricao(self):
    return self.descricao

  def getPreco(self):
    return self.preco

  def getEstoque(self):
    return self.estoque

  #Setters
  def setPreco(self,preco):
    self.preco = preco

  def setEstoque(self,estoque):
    self.estoque = estoque

#Node ou nó
class Node:
  #Construtor
  def __init__(self, label):
    self.label = label
    self.next = None

  #Getters
  def getLabel(self):
    return self.label

  def getNext(self):
    return self.next

  #Setters
  def setLabel(self, label):
    self.label = label

  def setNext(self, next):
    self.next = next


# LinkedList
class LinkedList:
  # Construtor
  def __init__(self):
    self.first = None
    self.len_list = 0

  # cria novo NODE
  def createNode(self, codigo):
    descricao = input("Informe a descrição: ")
    preco = input("Informe o preço: ")
    estoque = input("Informe o estoque")
    product = Produto(codigo, descricao, preco, estoque)
    node = Node(product)
    return node

  def verifyCode(self, codigo):
    aux = self.first
    while aux != None:
      if aux.getLabel().getCodigo() == codigo:
        return True
        break
      aux = aux.getNext()
    return False

  # OPÇÃO 1
  def insertStart(self, codigo):
    if self.verifyCode(codigo) == False:
      node = self.createNode(codigo)  # cria um novo nó

      # Lista vazia, simplesmente faz a LinkedList apontar para o novo node
      if self.empty():
        self.first = node
      # Lista não vazia, inserção no começo
      else:
        node.setNext(self.first)  # node apontar  para  o começo da lista
        self.first = node  # LinkedList apontar para o novo node
      self.len_list += 1
      print("código cadastrado no início com sucesso")
    else:
      print("código já cadastrado. Inserção não efetuada")

  # OPÇÃO 2
  def insertEnd(self):
    if self.verifyCode(codigo) == False:
      node = self.createNode(codigo)  # cria um novo nó

      # Lista vazia, simplesmente faz a LinkedList apontar para o novo node
      if self.empty():
        self.first = node
      # Lista não vazia, inserção no final
      else:
        aux1 = self.first
        aux2 = self.first.getNext()
        flag_insert = False
        while aux2 != None:
          aux1 = aux1.getNext()
          aux2 = aux2.getNext()
        # inserir no final
        aux1.setNext(node)
      self.len_list += 1
      print("código cadastrado no final com sucesso")
    else:
      print("código já cadastrado. Inserção não efetuada")

  # OPÇÃO 3
  def removeFirst(self):
    # Não remover de uma lista vazia
    if not self.empty():
      # Remover de uma lista com apenas 1 elemento
      if self.first.getNext() == None:
        self.first = None
      # Remover o primeiro node da lista
      else:
        self.first = self.first.getNext()
      self.len_list -= 1
      print("Produto removido do início com sucesso")

  # OPÇÃO 4
  def removeLast(self):
    # Não remover de uma lista vazia
    if not self.empty():
      # Remover de uma lista com apenas 1 elemento
      if self.first.getNext() == None:
        self.first = None
      # Remover do meio ou final da lista
      else:
        aux1 = self.first
        aux2 = self.first.getNext()
        while aux2.getNext() != None:
          aux1 = aux1.getNext()
          aux2 = aux2.getNext()
        aux1.setNext(None)
      self.len_list -= 1
      print("Produto removido do final com sucesso")

  # OPÇÃO 5
  def showAll(self):
    aux = self.first
    while aux != None:
      print(aux.getLabel().getCodigo(), end=' ')
      print(aux.getLabel().getDescricao(), end=' ')
      print(aux.getLabel().getPreco(), end=' ')
      print(aux.getLabel().getEstoque(), end=' ')
      print('')
      aux = aux.getNext()
    print('')

  # OPÇÃO 6
  def showProduct(self, codigo):
    aux = self.first
    while aux != None:
      if aux.getLabel().getCodigo() == codigo:
        print(aux.getLabel().getCodigo(), end=' ')
        print(aux.getLabel().getDescricao(), end=' ')
        print(aux.getLabel().getPreco(), end=' ')
        print(aux.getLabel().getEstoque(), end=' ')
        break
      aux = aux.getNext()
    print('')

  # OPÇÃO 7
  def alterProduct(self, codigo):
    aux = self.first
    while aux != None:
      if aux.getLabel().getCodigo() == codigo:
        while True:
          print("""Menu de opções para produto
            1 – Alterar Preço do produto
            2 – Alterar Estoque do produto
            0 – Sair do meno de alteração""")
          opt = input("Digite a opção: ")
          if opt == '1':
            preco = input("Informe o novo preço: ")
            aux.getLabel().setPreco(preco)
          elif opt == '2':
            estoque = input("Informe o novo valor de estoque: ")
            aux.getLabel().setEstoque(estoque)
          elif opt == '0':
            break
          else:
            print("Opção Inválida")
        break
      aux = aux.getNext()

  # OPÇÃO 8
  def remove(self, codigo):
    # Não remover de uma lista vazia
    if not self.empty():
      flag = False
      # Remover de uma lista com apenas 1 elemento
      if self.first.getNext() == None and self.first.getLabel().getCodigo() == codigo:
        self.first = None
        print("Produto removido do final com sucesso")
        flag = True

      # Remover de uma lista com mais de 1 elemento
      # Remover o primeiro node da lista
      elif self.first.getLabel().getCodigo() == codigo:
        self.first = self.first.getNext()
        print("Produto removido do final com sucesso")
        flag = True

      # Remover do meio ou final da lista
      else:
        aux1 = self.first
        aux2 = self.first.getNext()
        while aux2 != None:
          if aux2.getLabel().getCodigo() == codigo:
            aux1.setNext(aux2.getNext())
            print("Produto removido do final com sucesso")
            flag = True
            break
          aux1 = aux1.getNext()
          aux2 = aux2.getNext()
      if not flag:
        print("Produto não encontrado. Remoção não efetuada")
      self.len_list -= 1

  def empty(self):
    if self.len_list == 0:
      # if self.first == None
      return True
    return False

  def length(self):
    return self.len_list


ll = LinkedList()
while True:
  print("""Menu de opções
  1 – Inserir novo produto no início da lista
  2 – Inserir novo produto no final da lista
  3 – Remover o primeiro produto da lista
  4 – Remover o último produto da lista
  5 – Exibir todos os produtos da lista
  6 – Exibir os dados de um produto da lista
  7 – Alterar os dados de um produto da lista
  8 – Remover um produto da lista
  0 – Sair do programa""")
  opt = input("Digite a opção: ")
  if opt == '1':
    codigo = input("Informe o código: ")
    ll.insertStart(codigo)
  elif opt == '2':
    codigo = input("Informe o código: ")
    ll.insertEnd(codigo)
  elif opt == '3':
    ll.removeFirst()
  elif opt == '4':
    ll.removeLast()
  elif opt == '5':
    ll.showAll()
  elif opt == '6':
    codigo = input("Informe o código: ")
    ll.showProduct(codigo)
  elif opt == '7':
    codigo = input("Informe o código: ")
    ll.alterProduct(codigo)
  elif opt == '8':
    codigo = input("Informe o código: ")
    ll.remove(codigo)
  elif opt == '0':
    print("Programa Encerrado")
    break
  else:
    print("Opção Inválida")



