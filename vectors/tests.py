#
# # for i in a:
# #     b.append(random.sample(range(0, int(i)), 5))
# #
# # print(b)
#
# a = '10, 4, 70, 80, 50, 100, 150, 20, 45, 88'
#
#
# def test1(value):
#     print(value)
#     arr = value.split(',')
#     print(arr)
#     integers = [int(x) for x in arr]
#     print(integers)
#     valid = [x >= 10 for x in integers] # retorna TRUE OU FALSE para cada iten do array
#     print(valid)
#
#     if (all(valid)): # varifica se todos os itens do array sao True
#         print('All values are valid!')
#     if (not all(valid)): # oposto
#         print('Not all values are valid!')
#
# # test(a)
#
#
#
# def test(value):
#     valid = [int(x) >= 10 for x in value.split(',') ]
#     print(valid)
#
#     if (len(valid) != 10):
#         return False
#
#     if (not all(valid)):
#         return False
#     return True

# Fácil6. Leia uma matriz 4 x 4 e troque os valores
# da 1ª.linha pelos da 4ª.coluna, vice-e-versa. Escrever ao final a matriz obtida
import numpy as np

# matrice = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]


# def trocaLinhaB(b,inicio,final):
#     listaAux = b[inicio]
#     b[inicio] = b[final]
#     b[final] = listaAux


# def trocaLinhaB(b,inicio,final):
#     listaAux = b[inicio].copy()  # <= aqui: cria uma cópia
#     b[inicio] = b[final]
#     b[final] = listaAux
#
# trocaLinhaB(matrice)

# for l in matrice:
#     for c in matrice:
#
#
#
# print(matrice)

# matrice = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9],
#            [7, 8, 9]]
#
# # a = np.array([[4,3,1], [5,7,0], [9,9,3], [8,2,4]])
# # for l in matrice:
# #     # for c in matrice:
# #     matrice[[0, 3]] = matrice[[3, 0]]
# matrice[[0, 3]] = matrice[[3, 0]]

# print(matrice)


# Fácil6. Leia uma matriz 4 x 4 e troque os valores
# da 1ª.linha pelos da 4ª.coluna, vice-e-versa. Escrever ao final a matriz obtida

matrice = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])

matrice[[0, 3]] = matrice[[3, 0]]
# print(matrice)

matrix = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [70, 80, 90]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 17, 12]]
matrix[0], matrix[-1] = matrix[-1], matrix[0]
# print(matrix)


matrixx = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [70, 80, 90]]

a = []

for i in matrixx:
    matrixx[0], matrixx[-1] = matrixx[-1], matrixx[0]
# print(matrixx)

a = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [70, 80, 90]]

def trocaLinhaB(b,inicio,final):
    listaAux = b[inicio].copy()  # <= aqui: cria uma cópia
    b[inicio] = b[final]
    b[final] = listaAux

# trocaLinhaB(b)

matrix = [[1, 2, 3],
    [4, 5, 6]]


# def col_swapper(matrix, col_1, col_2):
#     for line in range(len(matrix)):
#         matrix[line][col_1], matrix[line][col_2] = matrix[line][col_2], matrix[line][col_1]
#
# print(matrix)
# col_swapper(matrix)

# for l in range(len(matrix)):
#     for c in range(len(matrix)):
#         matrix[l][c[1]], matrix[l][c[2]] = matrix[l][c[2]], matrix[l][c[1]]
#
# print(matrix)

a = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

b = []

for i in range(4):
    t = a[0][i]
    a[0][i] = a[3][i]
    a[3][i] = t
    b = a

print(a)

k = [1,2,3]
print(len(k))