"""solicite ao usuário 3 numeros, armazene em uma lista e apresente o menor e maior elemento"""

lista = []

for i in range(3):
    valor = int(input(f'Digite o valor {i+1}: '))
    lista.append(valor)

maior = lista[0]
menor = lista[0]

for i in range(1, 3):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]

print('Menor valor:', menor)
print('Maior valor:', maior)
