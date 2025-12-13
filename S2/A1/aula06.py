"""Aula 06 - Conversão de Tipos"""

# Conversão de tipo implicita e explicita

leitura = 5.53
peso = 3
total = leitura * peso
print(total, type(total))

# Conversão explícita (type casting)
soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = '32'
print(idade, type(idade))

idade = int('32')
print(idade, type(idade))

nome = 'Maria'
altura = 1.70

mensagem = f'{nome} tem a altura de {altura}'
print(mensagem)
