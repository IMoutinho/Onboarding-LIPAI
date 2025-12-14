"""Aula 02 - Arguments: positional, keyword, default value"""

# declara uma funcao que soma dois numeros


def somar(n1, n2):
    return n1+n2


def dividir(dividendo, divisor):
    return dividendo/divisor


# Argumentos posicionais
print(somar(10.0, 3.5))
print(somar(2.0, 6.5))
print(dividir(10, 2))

# unpack list e tuplas
numeros = [10.0, 5.5]
print('somar numeros de uma lista', somar(numeros[0], numeros[1]))
print('somar numeros de uma lista', somar(*numeros))

# unpack dict
numeros = {
    "n1": 10.2,
    "n2": 5.3
}
print('somar numeros de um dict', somar(**numeros))


# argumentos nomeados(keyword)
print(somar(n1=3.0, n2=6.2))
print(somar(n2=5.0, n1=7.8))
print(dividir(divisor=3, dividendo=10))

# Declaracao
# nome: saudacoes:
# parametros: nome, saudacao
# retorno: string


def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao}, {nome}'


print(saudacoes('João', 'Olá'))
print(saudacoes('Maria', 'Bom dia'))
print(saudacoes('Pedro'))

print(saudacoes(saudacao='Oi Oi', nome='Marcio'))
print(saudacoes(nome='Karina'))
