"""ex03.py - verificação de validade de identificador"""

identificador = input('Digite o identificador:')

VERIFICA_TAMANHO = len(identificador) == 7
VERIFICA_BR = identificador[0] == 'B' and identificador[1] == 'R'
valorInteiro = identificador[2:6]
VERIFICA_INTEIRO = 1 <= int(valorInteiro) <= 9999
VERIFICA_ULTIMO = identificador[6] == 'X'

if not VERIFICA_TAMANHO:
    print('Tamanho indevido')

elif not VERIFICA_BR:
    print('O identificador não inicia com a sequência BR')

elif not VERIFICA_INTEIRO:
    print('O identificador não apresenta número inteiro entre 0001 e 9999')

elif not VERIFICA_ULTIMO:
    print('O identificador não finaliza com caractere X')

else:
    print('Identificador válido!')
