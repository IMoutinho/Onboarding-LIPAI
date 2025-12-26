"""Aula 04 - Tipos de Dados - Dics"""

# dic (dicionário)
# coleção de key-value(chave-valor)
# key é única
# mutaveis

# criar um dic

carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

print(carro, type(carro))

# acessar valores por chave
print(carro["marca"])
print(carro.get("marca"))

# pegar todas as chaves, valores e pares
print(carro.keys())
print(carro.values())
print(carro.items())

# verifica se a chave existe
print("cor" in carro)
print("marca" in carro)

# adicionar chave/valor de forma dinamica
carro["cor"] = 'Azul'

print("cor" in carro)
print(carro, type(carro))

# remover uma chave
marca = carro.pop("marca")
print(carro)
print(marca)

# loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

for key, value in carro.items():
    print(key, value)


# lista de dicionarios

aluno1 = {
    'nome': 'João',
    'email': 'joao@email.com',
    'notas': [10.0, 5.3, 7.0]
}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@email.com',
    'notas': [10.0, 8.3, 7.2]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)
