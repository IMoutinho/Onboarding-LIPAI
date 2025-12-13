""""ex02 - calculando media aritmetica"""

n = input('Digite as notas (separadas por um espaço): ').split()
soma = 0.0
for nota in n:
    soma = soma + float(nota)

media = soma/len(n)

print('A média das notas é:', media)

SITUACAO_APROVADO = media > 6.0
SITUACAO_REPROVADO = media < 4.0

if SITUACAO_APROVADO:
    print('Aprovado!')
elif SITUACAO_REPROVADO:
    print('Reprovado!')
else:
    print('Recuperacao')
