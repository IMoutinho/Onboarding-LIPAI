"""Calculadora de IMC"""


def calcular_imc(pessoa):
    """Calcula imc dic"""
    p = float(pessoa['peso'])
    a = float(pessoa['altura'])
    return p/(a*a)


def obter_classificacao(imc):
    """verifica classificacao imc"""
    if (imc < 18.5):
        print('Baixo peso')
    elif (18.5 <= imc <= 24.9):
        print('Peso normal')
    elif (25.0 <= imc <= 29.9):
        print('Excesso de peso')
    elif (30.0 <= imc <= 34.9):
        print('Obesidade de Classe 1')
    elif (35.0 <= imc <= 39.9):
        print('Obesidade de classe 2')
    else:
        print('Obesidade de classe 3')


def situacao_individuo(imc):
    """verificia situacao imc"""
    if (imc < 18.5):
        print('Ganhar peso')
    elif (18.5 <= imc <= 24.9):
        print('Normal')
    else:
        print('Perder peso')


pesok = input('Digite seu peso: ')
tamanho = input('Digite sua altura(em metros): ')

individuo = {
    'altura': tamanho,
    'peso': pesok
}

valor_imc = calcular_imc(individuo)
print(valor_imc)
obter_classificacao(valor_imc)
situacao_individuo(valor_imc)
