def linha_para_dict(linha, chaves):
    dados = linha.strip().split(',')
    resultado = {}

    for i in range(len(chaves)):
        resultado[chaves[i]] = dados[i]

    return resultado


teste1 = linha_para_dict(
    "SP000001,Maria da Silva,maria@email.com", ['prontuario', 'nome', 'email'])
print(teste1)

teste2 = linha_para_dict("banana,3", ['item', 'quantidade'])
print(teste2)
