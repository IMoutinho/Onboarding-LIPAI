"""função que recebe uma tupla de numeros e retorna a soma"""


def soma_tupla(tupla):
    acumula = 0
    for valores in tupla:
        acumula += valores
    return acumula

numeros=(1,2,3,4,6)
print(soma_tupla(numeros))
