"""" Aula 02 - instrução if"""

# if condição:
#   instrucao
#   instrucao

codigo_cliente = 32
valor_desconto = 30.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

# if desconto >= 20.0:
#     print('Desconto Especial!')

if DESCONTO_ESPECIAL:
    print('Desconto Especial!')
    print(codigo_cliente)
else:
    print('Sem Desconto Especial!')

# nome tem que ter pelo menos 3 caracteres
nome = 'Lo'

NOME_INVALIDO = len(nome) < 3
NOME_VALIDO = len(nome) >= 3

print(len(nome), type(len(nome)))

if NOME_INVALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido!')

if NOME_VALIDO:
    print('Nome válido!')
else:
    print('Nome deve ter pelo menos 3 caracteres')

if not NOME_VALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido!')


# nome tem que ter peço menos 3 caracteres
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas

nome = 'Lo'
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append('Idade deve ser maior ou igual a 18')

# False: False, None, 0, 0.0, string vazia '', lista, tupla, dicionário vazios
if len(erros) != 0:
    print(erros)
else:
    print('Dados válidos!')


# if elif else

# verifica se um numero é positivo ou negativo ou zero
numero = 3

if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')

# calcule a média e verifique se as duas notas
# sao validas antes do calculo
n1 = 5.6
n2 = 10.0

if n1 >= 0 and n1 <= 10.0:
    if n2 >= 0 and n2 <= 10.0:
        media = (n1 + n2) / 2
        if media >= 6:
            print('Aprovado')
        elif media >= 4:
            print('Recuperação')
        else:
            print('Reprovado')
    else:
        print('Notas inválidas')
else:
    print('Notas inválidas')

if 0 <= n1 <= 10.0 and 0 <= n2 <= 10.0:
    media = (n1 + n2) / 2
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')

NOTA1_VALIDA = 0 <= n1 <= 10.0
NOTA2_VALIDA = 0 <= n2 <= 10.0

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')
