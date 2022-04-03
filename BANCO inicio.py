import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'Data Abertura: {self.data_abertura}')
        print(f'Transações: ')
        for i in self.transacoes:
            print('-', i)


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Contas:
    def __init__(self, numero, cliente, saldo, limite=1000):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposito(self, valor):
        self.saldo+= valor
        self.historico.transacoes.append(f'Deposito de {valor}')


    def saque(self, valor):
        if self.saldo < valor:
            print(f'Saldo insuficiente para o saque\nSeu saldo é {conta.saldo}')
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'Saque de {valor}')


    def extrato(self):
        print(f'Conta: {self.numero}\nSaldo: {self.saldo:.2f}')
        self.historico.transacoes.append(f'Tirou extrato - Saldo de {self.saldo}')

    def transfere(self, destino, valor):
        retirou = self.saque(valor)
        if retirou == False:
            return False
        else:
            destino.deposito(valor)
            self.historico.transacoes.append(f'Transferencia de {valor} para conta de {destino.numero}')
            return True


cliente1 = Cliente('Fulano', 'detal', '123.321.456-78')
cliente2 = Cliente('ze', 'mane', '789.987.456.32')
conta1 = Contas('12345-5', cliente1, 1000.00)
conta2 = Contas('98745-3', cliente2, 1000.00)


conta1.deposito(100)
conta1.saque(50)
conta1.transfere(conta2, 200)
conta1.extrato()
conta1.historico.imprime()

conta2.historico.imprime()



