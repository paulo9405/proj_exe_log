
# for i in a:
#     b.append(random.sample(range(0, int(i)), 5))
#
# print(b)

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
