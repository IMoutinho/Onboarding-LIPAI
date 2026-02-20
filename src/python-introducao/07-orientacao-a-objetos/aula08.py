'''Aula 08 - Herança'''


class Pessoa:  # SUPERCLASSE
    def __init__(self, nome, sobrenome, cpf):
        print("Entrei no SUPER CONSTRUTR")
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):  # SUBCLASSE
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcula_pagamento(self):
        return self.salario - ((10/100) * self.salario)


class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento()
        return pagamento_salario + self.bonus


cliente = Cliente("Paulo", "Mulotto", "123.456.789-00")
print(cliente.obtem_nome_completo())

funcionario = Funcionario("Ana", "Silva", "987.654.321-00", 50000)
print(funcionario.obtem_nome_completo())
print(funcionario.calcula_pagamento())

progamador = Programador("Carlos", "Santos", "111.222.333-44", 70000, 200)
print(progamador.obtem_nome_completo())
print(progamador.calcula_pagamento())
