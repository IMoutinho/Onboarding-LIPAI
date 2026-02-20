# open("caminho", "r")

# Mode
# r - read - leitura
# w - write - escrita (apaga o conteudo anterior)
# a - append - acrescentar conteudo
# x - create - criar arquivo
# r+ - leitura e escrita

# arquivo = open("s3/src/06-arquivos/test3.txt", "x")

# print(arquivo.readable())  # Verifica se o arquivo pode ser lido

# print(arquivo.readline())  # Lê uma linha do arquivo
# print(arquivo.readline())
# print(arquivo.readline())

# list = arquivo.readlines()  # Lê todas as linhas e retorna uma lista

# print(list)

# print(list[3])  # Imprime a linha de índice 3 da lista

# arquivo.write("SQL\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# arquivo.close()

import os

# if os.path.exists("s3/src/06-arquivos/test2.txt"):
os.remove("s3/src/06-arquivos/test2.txt")
# else:
#   print("O arquivo não existe")

# os.rmdir("s3/src/nova_pasta")  # Remove uma pasta vazia
