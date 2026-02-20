import numpy as np
from numpy.random import default_rng
from time import process_time
import matplotlib.pyplot as plt


a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a)
print(type(a))
print('\n=====================================')

b = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9, 7]])
print(b)
print(type(b))
print('\n=====================================')

# np.zeros
# um objeto de 3 dimensões
zero_array = np.zeros(shape=(5, 3, 6))
print(zero_array)

print('\n=====================================')

# np.ones
um_array = np.ones((2, 3))
print(um_array)
print('\n=====================================')

# np.empty
vazio = np.empty((3, 4))
print(vazio)
print('\n=====================================')

# np.arrange
arr = np.arange(50, 200, 30)
print(arr)
print('\n=====================================')

arr2 = np.arange(step=30, start=50, stop=200)
print(arr2)
print('\n=====================================')

arr1 = np.arange(10)
print(arr1)
print('\n=====================================')

# np.linspace

array_linear = np.linspace(0, 100, num=20, endpoint=False)
print(array_linear)
print('\n=====================================')

# considera o último valor colocado como ponto de parada, caso use endpoint = True
array_linear1 = np.linspace(0, 100, num=20, endpoint=True)
print(array_linear1)
print('\n=====================================')

# retstep mostra o espaçamento que há de um para outro
array_linear2 = np.linspace(0, 100, num=40, endpoint=False, retstep=True)
print(array_linear2)
print('\n=====================================')

# descobrindo tamanho de um array
# forma
print(zero_array.shape)

print('\n=====================================')
# tamanho (quantidade de valores)
print(zero_array.size)
print('\n=====================================')
# quantidade de dimensões
print(zero_array.ndim)
print('\n=====================================')

# transformando um vetor de 1d em uma matriz 2d
d = np.array([1, 2, 3])
print(d)
print(d.shape)
print(d.ndim)
print('\n=====================================')

d2 = d[np.newaxis, :]
print(d2.shape)
print(d2.ndim)
print(d2)
print('\n=====================================')

d22 = d[:, np.newaxis]
print(d22.shape)
print(d22.ndim)
print(d22)
print('\n=====================================')

print(d22[0][0])

# concatenando arrays

d = np.array([1, 2, 3])
e = np.array([4, 5, 6])

f = np.concatenate((d, e))
g = np.concatenate((e, d))

print('\n=====================================')
print(f)
print('\n=====================================')
print(g)
print('\n=====================================')


# consultando itens de um array

g = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(g)
print('\n=====================================')
# printa de acordo com um valor selecionado, no caso maior que 8
maior_8 = g[g > 8]
print(maior_8)
print('\n=====================================')

# operações om array

g = np.array([1, 2, 3])
# soma
print(g.sum())
# maximo
print(g.max())
# menor
print(g.min())
# media
print(g.mean())
print('\n=====================================')

# gerando amostras aleatorias


rng = default_rng()
aleatorio = rng.integers(100, size=(2, 4))
print(aleatorio)

print('\n=====================================')

# diferença entre array e lista
h = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(h)
print(type(h))

print('\n=====================================')

lista_h = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista_h)
print(type(lista_h))

# para manter a homogeneidade o array transofrma todos os itens em string, para melhor processamento
h = np.array([1, 'Daniel', 3, 4, 5, 6, 7, 8])
print(h)
print(type(h))

print('\n=====================================')

# a lista permite que se tenha mais de um tipo de item dentro dela, tanto que foi impresso como string e inteiro
lista_h = [1, 'Daniel', 3, 4, 5, 6, 7, 8]
print(lista_h)
print(type(lista_h))

# comparando o processamento
lista_h = list(rng.integers(10, 100, 10000000))
lista_i = list(rng.integers(10, 100, 10000000))
j = []

t1 = process_time()
for i in range(len(lista_h)):
    j.append(lista_h[i]*lista_i[i])
t2 = process_time()

print(t2-t1)

print('\n=====================================')


lista_k = rng.integers(10, 100, 10000000)
lista_l = rng.integers(10, 100, 10000000)

t1m = process_time()
m = lista_k * lista_l
t2m = process_time()

print(t2m-t1m)

#

dados_x = rng.integers(20, size=30)
dados_y = rng.integers(12, size=30)

plt.scatter(x=dados_x, y=dados_y)
plt.show()
