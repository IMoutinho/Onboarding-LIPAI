"""funcao que recebe varios argumentos numericos atraves de *args e retorna a soma dos numeros"""


def soma_args(*n):
    acumula = 0
    for valores in n:
        acumula += int(valores)
    return acumula


valor = input('Digite os valores, separados por espaço: ').split()
print(soma_args(*valor))
