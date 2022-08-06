'''
a = '10, 4, 70, 80, 50, 100, 150, 20, 45, 88'


def test1(value):
    print(value)
    arr = value.split(',')
    print(arr)
    integers = [int(x) for x in arr]
    print(integers)
    valid = [x >= 10 for x in integers] # retorna TRUE OU FALSE para cada iten do array
    print(valid)

    if (all(valid)): # varifica se todos os itens do array sao True
        print('All values are valid!')
    if (not all(valid)): # oposto
        print('Not all values are valid!')

v = test1(a)
#
print(v, 'v')


def test(value):
    valid = [int(x) >= 10 for x in value.split(',') ]
    print(valid)

    if (len(valid) != 10):
        return False

    if (not all(valid)):
        return False
    return True

a = '10, 4, 70, 80, 50, 100, 150, 20, 45, 88'

def test3(value):
    valid = [int(x)for x in value.split(',') ]
    return


c = test3(a)

print(c, 'c')
'''





'''
Leia duas matrizes 4 x 4 e escreva uma terceira com
 os 4 maiores elementos entre as primeiras
'''


import random
import numpy as np
a = '10, 15, 70, 80'


def test1(value):
    arr = value.split(',')
    integers = [int(x) for x in arr]
    valid = [x >= 10 for x in integers]

    if (not all(valid)): # oposto
        print('Not all values are valid!')

    matrices = []
    for x in integers:
        matrices.append([random.randint(1, x) for _ in range(5)])

    max_line = np.array(matrices)
    # axis=1 to find max from each row
    x = np.amax(max_line, axis=1)
    b = []
    for i in x:
        b.append(i)
    matrices.append(b)

    print(matrices)

print(test1(a))
print('---------------------------------------------')

# f = [[0,8,4], [5,88,1], [1,5,9]]
# import numpy as np
# a = np.array(f)
# # axis=1 to find max from each row
# x = np.amax(a, axis=1)
# print(x)


