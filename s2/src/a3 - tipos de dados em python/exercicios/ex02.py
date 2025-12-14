"""Solicite ao usuário o mes do ano em formato numerico e retorne o nome"""

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

mes = int(input('Digite o número do mês: '))

print(meses[mes-1])
