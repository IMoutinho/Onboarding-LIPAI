"""aula 01 - Introdução à funções"""

# Funcao é um bloco que realiza uma tarefa especifica
# dividir o problema em pequenas partes
# evitar duplicacao de codigo

# 1. Standart Library Functions - built-in Functions
# ex: print, len

print('Olá', 123, True)

nomes = ['João', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User Defined Functions
# Definidas pelo desenvolvedor(a)
# Fazerem parte da solução do problema

# declara
# nome: saudacoes
# parametros: nenhum
# retorno: nenhum


def saudacoes():
    print('Olá!!!!!')


# chamada
saudacoes()
saudacoes()
saudacoes()

# declara
# nome: saudacoes
# parametros: nenhum
# retorno: nenhum


def saudacoesp(nome):
    """saudacao"""
    print(f'Olá, {nome}')


# chamada
# valores, variaveis, expressoes => argumentos
# 'Maria' é um argumento passado para o parametro nome
saudacoesp('Maria')
saudacoesp('Pedro')
x = 'Carlos'
saudacoesp(x)

# declaração
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: nenhum


def calcular_media(nota1, nota2, nota3):
    """Calculo da Media"""
    media = ((nota1+nota2+nota3)/3)
    print(media)


# chamada
# argumentos são literais
calcular_media(10.0, 3.0, 6.0)

# chamada
# argumentos são variaveis
N1 = 10.0
N2 = 3.2
N3 = 5.6
calcular_media(N1, N2, N3)


def calcular_mediar(nota1, nota2, nota3):
    """Retorna a media de 3 notas""" 
    mediar = ((nota1+nota2+nota3)/3)
    return mediar 



MEDIAR = calcular_mediar(10.0, 3.0, 6.0)
print('Valor da média: ', MEDIAR)
# enviar no email
# salvar no banco de dados
# salvar no arquivo
