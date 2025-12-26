# arq = open('arquivo.txt', 'w')

# string = 'Olá, Caio! Tudo bem?'

# lista = ['Olá, Caio!\n', 'Tudo bem?\n', 'Espero que sim!\n']

# arq.write('Olá, Tudo bem?\n')
# arq.write('Caio\nMarcos\nJoão\n')

# arq.writelines(lista)

# print(lista)

# arq.close()

with open('arquivo.txt', 'a') as arq:
    arq.write('\ncaio')

with open('arquivo.txt', 'r') as arq:
    # X = arq.readlines()
    # print(X)
    x = arq.read()
    print(x)
    print(type(x))

with open('arquivo.txt', 'rb') as arq:
    for i in arq:
        print(i)


print('fim')
