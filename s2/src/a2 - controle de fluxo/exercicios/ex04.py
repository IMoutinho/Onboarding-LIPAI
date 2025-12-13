"""utilizando de base o exercicio validador anterior, criar uma lista de erros"""

erro = ['Tamanho indevido', 'O identificador não inicia com a sequência BR',
        'O identificador não apresenta número inteiro entre 0001 e 9999', 'O identificador não finaliza com caractere X']
identificador = input('Digite o identificador:')

VERIFICA_TAMANHO = len(identificador) == 7
VERIFICA_BR = identificador[0] == 'B' and identificador[1] == 'R'
valorInteiro = identificador[2:6]
VERIFICA_INTEIRO = 1 <= int(valorInteiro) <= 9999
VERIFICA_ULTIMO = identificador[6] == 'X'
IDENTIFICADOR_VALIDO = VERIFICA_BR and VERIFICA_INTEIRO and VERIFICA_TAMANHO and VERIFICA_ULTIMO


if not IDENTIFICADOR_VALIDO:
    if not VERIFICA_TAMANHO:
        print(erro[0])
    if not VERIFICA_BR:
        print(erro[1])
    if not VERIFICA_INTEIRO:
        print(erro[2])
    if not VERIFICA_ULTIMO:
        print(erro[3])

else:
    print('Identificador válido')
