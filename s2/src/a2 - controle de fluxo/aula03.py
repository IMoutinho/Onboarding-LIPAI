""" Aula 03 - Loop for"""

# 1. Repetir instrução
# 2. Iteração em coleção de elementos (repetir instrução)

linguagens = ['C', 'Python', 'Java']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for valor in colecao:
#   instrucoes
#   instrucoes

for linguagem in linguagens:
    print(linguagem.upper())

# comportamento do operador in é
# diferente com base no contexto
print('Java' in linguagens)

notas1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (notas1 + nota2 + nota3) / 3
print(media)

notas = [10.0, 5.5, 8.3]

soma = 0.0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(media)

# range
# valores = range(10)
# valores = range(0, 10)
# valores = range(0, 10, 2)
valores = range(9, 0, -1)
print(valores)

for valor in valores:
    print(valor)

for i in range(len(linguagens)):
    print(linguagens[i])
