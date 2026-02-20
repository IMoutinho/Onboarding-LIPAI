"""Aula 02 - Atributs de classe e instancia"""

# classe Pessoa possui atributos de instância: nome e email


class Pessoa:
    especie = 'Humano'  # atributo de classe

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')
pessoa3 = Pessoa('Pedro Santos', 'pedro@email.com')

# alterar um atributo de classe na instancia (objeto) altera somente para aquela instancia
pessoa1.especie = 'Alienígena'

# alterar um atributo de classe na classe altera todos objetos e na classe também
Pessoa.especie = 'Alienigenas do Passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print(pessoa3.nome, pessoa3.email, pessoa3.especie)

print(Pessoa.especie)
