'''Aula 07 - Relacionamento entre classes'''


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone[ddd = {self.ddd}, numero = {self.numero}]'


class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco[cep = {self.cep}, numero = {self.numero}]'


class Pessoa:
    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = []

    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf = {self.cpf}, nome = {self.nome}, telefone = {self.telefone}]'


telefone = Telefone('11', '99999-9999')
pessoa1 = Pessoa('1233233', 'João da Silva', telefone)
pessoa1.add_endereco(Endereco('12345-678', 123))
pessoa1.add_endereco(Endereco('98765-432', 456))

pessoa2 = Pessoa('122233233', 'Maria da Silva', telefone)
pessoa2.add_endereco(Endereco('54321-876', 789))

print(pessoa1)
print(pessoa2)
print(pessoa1.nome, pessoa1.cpf, pessoa1.telefone)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)

pessoa1.print_enderecos()
pessoa2.print_enderecos()
