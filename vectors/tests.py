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
#
#
# matrices = [
#             [0, 0, 0, 0, 0, ],
#             [0, 0, 0, 0, 0, ],
#             [0, 0, 0, 0, 0, ],
#             [0, 0, 0, 0, 0, ],
#             [0, 0, 0, 0, 0, ],
#             ]
#
# linha = coluna = 0
#
# for _ in range(0, len(matrices)):
#     matrices[linha][coluna] = 1
#     linha += 1
#     coluna += 1
#
# for l in range(0, len(matrices)):
#     for c in range(0, len(matrices)):
#         print(matrices[l][c], end=' ')
#     print()
#
#
# print()
#


# (0,0)
# (1,0) (1,1)
# (2,0) (2,1) (2,2)
# (3,0) (3,1) (3,2) (3,3)
# (4,0) (4,1) (4,2) (4,3) (4,4)

m = 1
lista = list()
for i in range(1, m + 1):
    linha = list()
    for j in range(1, m + 1):
        if i > j:
            linha.append(0)


f = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# (0,0)
# (1,0) (1,1)
# (2,0) (2,1) (2,2)
# (3,0) (3,1) (3,2) (3,3)
# (4,0) (4,1) (4,2) (4,3) (4,4)

matriz = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            ]

for l in range(len(matriz)):
    for c in range(len(matriz)):
        if c < l:
            matriz[c][l] = 0

for l in matriz:
    print(l)



