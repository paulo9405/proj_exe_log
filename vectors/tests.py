
# for i in a:
#     b.append(random.sample(range(0, int(i)), 5))
#
# print(b)
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

# test(a)



def test(value):
    valid = [int(x) >= 10 for x in value.split(',') ]
    print(valid)

    if (len(valid) != 10):
        return False

    if (not all(valid)):
        return False
    return True
'''

# count = 0
# a = [4, 5, 8, 4, 9, 4]
#
# for i in a:
#     if 4 in a:
#         count += i

# print(count)
# print(a.count(4))

count = 0
matrice = [[4, 5, 80, 40, 19, 14], [4, 5, 80, 4, 19]]
b = []
for l in matrice:
    for c in l:
        if c > 10:
            b.append(c)
            count += 1

print(count)
print(b)