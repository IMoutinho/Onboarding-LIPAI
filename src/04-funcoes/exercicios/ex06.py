"""Calcula o volume do aquario, potencia do termostato necessario, quantidade de filtragem necessaria por hora"""


def volume_aquario(n):
    c = float(n['Comprimento'])
    a = float(n['Altura'])
    l = float(n['Largura'])
    return (c*a*l)/1000


def potencia_termostato(v, n):
    t_d = float(n['Temperatura desejada'])
    t_a = float(n['Temperatura ambiente'])
    return v * 0.05 * (t_d - t_a)


def filtragem_aquario(v):
    return 3*v


comprimento_aquario = input('Digite o comprimento do aquario: ')
altura_aquario = input('Digite a altura do aquario: ')
largura_aquario = input('Digite a largura do aquario: ')
temperatura_ambiente = input('Digite a temperatura ambiente atual: ')
temperatura_desejada = input('Digite a temperatura desejada para o aquario: ')

aquario = {
    'Comprimento': comprimento_aquario,
    'Altura': altura_aquario,
    'Largura': largura_aquario,
    'Temperatura ambiente': temperatura_ambiente,
    'Temperatura desejada': temperatura_desejada
}

volume = volume_aquario(aquario)
potencia = potencia_termostato(volume, aquario)
filtragem = filtragem_aquario(volume)

for key in aquario:
    print(key, ':', aquario[key])
    print('---------------------------------------')

print('Volume total do aquario:', volume, 'litros')
print('---------------------------------------')
print('Potencia do termostato necessária: ', potencia)
print('---------------------------------------')
print('Filtragem por hora necessária: ', filtragem)
print('---------------------------------------')
