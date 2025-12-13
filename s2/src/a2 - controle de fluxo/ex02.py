#solicite ao usuário 3 notas e apresente o resultado da média aritmética dessas notas

n1 = input('Digite a primeira nota: ')
n2 = input('Digite a segunda nota: ')
n3 = input('Digite a terceira nota: ')

media = (float(n1) + float(n1) + float(n3)) / 3
print (f'A média aritmética das notas é: {media}')  

if media >6.0:
    print('Aprovado')
    else if (media >=4.0) and (media <=6.0):
        print('Recuperação')
        else:
            print('Reprovado')
    