"""solicitar ao usuário o mês em inteiro e retornar em string usando dic"""

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}


mes = int(input('Digite o número do mês: '))
mesextenso = meses[mes]
print(mesextenso)
