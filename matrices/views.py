from django.shortcuts import render
import random


def home(request):
    return render(request, 'matrices/home.html')


def matrice_ex1(request):
    if request.method != 'POST':
        return render(request, 'matrices/matrice_ex1.html')

    value = request.POST.get('value1').split(',')

    if len(value) != 10:
        error = 'Plaese write just 10 values.'
        return render(request, 'matrices/matrice_ex1.html', {'error': error})

    integers = [int(x) for x in value]
    valid = [x >= 10 for x in integers]

    if (not all(valid)):
        error = 'Plaese write values grater than 9.'
        return render(request, 'matrices/matrice_ex1.html', {'error': error})

    matrices = []
    for x in integers:
        matrices.append([random.randint(1, x) for _ in range(10)])

    maior = 0
    for i in range(0, len(matrices)):
        for j in range(0, len(matrices)):
            if matrices[i][j] > maior:
                maior = matrices[i][j]
                position = i, j

    return render(request, 'matrices/matrice_ex1.html', {'matrices': matrices, 'maior': maior, 'position': position})


def matrice_ex2(request):
    matrices = []
    if request.method == 'POST':
        value1 = request.POST.get('value1').split(',')

        for i in value1:
            int_i = int(i)
            if int_i != 1:
                error = 'Plaese write just number 1.'
                return render(request, 'matrices/matrice_ex2.html', {'error': error})

        matrices = [
            [0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, ],
            ]

        linha = coluna = 0

        for _ in range(0, len(matrices)):
            matrices[linha][coluna] = int_i
            linha += 1
            coluna += 1

    return render(request, 'matrices/matrice_ex2.html',   {'matrices': matrices})
    
    
def matrice_ex3(request):
    matrices_1 = []
    matrices_2 = []
    matrice_third = []
    lem = None

    if request.method == 'POST':
        value1 = request.POST.get('value1').split(',')
        value2 = request.POST.get('value2').split(',')
        value3 = request.POST.get('value3').split(',')
        value4 = request.POST.get('value4').split(',')

        value5 = request.POST.get('value5').split(',')
        value6 = request.POST.get('value6').split(',')
        value7 = request.POST.get('value7').split(',')
        value8 = request.POST.get('value8').split(',')

        lem = len(value1+value2+value3+value4+value5+value6+value7+value8)

        if lem != 32:
            error = 'Please write just 4 values in each field.'
            return render(request, 'matrices/matrice_ex3.html', {'error': error})

        matrices_1 = [value1, value2, value3, value4]
        matrices_2 = [value5, value6, value7, value8]

        largest_a = []
        for linha in matrices_1:
            largest_a.append(max(linha))

        list_sorted_a = sorted(largest_a)
        largest_first_a = list_sorted_a[-1]
        largest_second_a = list_sorted_a[-2]

        largest_b = []
        for linha in matrices_2:
            largest_b.append(max(linha))

        list_sorted_b = sorted(largest_b)
        largest_first_b = list_sorted_b[-1]
        largest_second_b = list_sorted_b[-2]

        matrice_third = [[largest_first_a, largest_second_a], [largest_first_b, largest_second_b]]

    return render(request, 'matrices/matrice_ex3.html', {'matrices_1': matrices_1,
                                                         'matrices_2': matrices_2,
                                                         'matrice_third': matrice_third, 'lem':lem})


def matrice_ex4(request):
    matrices = []
    larger_than_ten = []
    count = None


    if request.method == 'POST':
        value1 = request.POST.get('value1').split(',')
        value2 = request.POST.get('value2').split(',')
        value3 = request.POST.get('value3').split(',')
        value4 = request.POST.get('value4').split(',')
        value5 = request.POST.get('value5').split(',')
        value6 = request.POST.get('value6').split(',')

        lem = len(value1 + value2 + value3 + value4 + value5 + value6)

        if lem != 36:
            error = 'Plaese write just 6 values in each field.'
            return render(request, 'matrices/matrice_ex4.html', {'error': error})

        matrices = [value1, value2, value3, value4, value5, value6]
        larger_than_ten = []
        count = 0


        for l in matrices:
            for c in l:
                if int(c) > 10:
                    larger_than_ten.append(c) # or i can use the len of this will return the quantity.
                    count += 1

    return render(request, 'matrices/matrice_ex4.html', {'matrices': matrices,
                                                         'larger_than_ten': larger_than_ten,
                                                         'count': count
                                                         })


def matrice_ex5(request):
    matrices = []
    error2 = None
    value2_int = None

    if request.method == 'POST':
        value1 = request.POST.get('value1').split(',')
        value2 = request.POST.get('value2').split(',')
        value3 = request.POST.get('value3').split(',')
        value4 = request.POST.get('value4').split(',')
        value5 = request.POST.get('value5').split(',')

        lem = len(value1 + value2 + value3 + value4 + value5)
        if lem != 25:
            error = 'Plaese write just 5 values.'
            return render(request, 'matrices/matrice_ex5.html', {'error': error})

        matrices = [value1, value2, value3, value4, value5]

        valueX = request.POST.get('valueX').split(',')

        value2_int = int(valueX[0])

        for i in range(0, len(matrices)):
            for j in range(0, len(matrices)):
                if matrices[i][j] == value2_int:
                    position = i, j

                    return render(request, 'matrices/matrice_ex5.html', {
                        'matrices': matrices, 'position': position, 'value2_int': value2_int})

            error2 = 'not in matrice.'
    return render(request, 'matrices/matrice_ex5.html', {'matrices': matrices, 'error2': error2, 'value2_int': value2_int})


def matrice_ex6(request):
    value = []
    if request.method == 'POST':
        value = request.POST.get('value').split(',')

    if len(value) != 4:
        error = 'Plaese write just 4 values.'
        return render(request, 'matrices/matrice_ex6.html', {'error': error})

    matrices = []
    for i in value:
        int_i = int(i)

        if int_i < 4:
            error = 'Plaese write value grater than 4.'
            return render(request, 'matrices/matrice_ex6.html', {'error': error})

        matrices.append([random.randint(1, int_i) for _ in range(4)])

    for i in range(4):
        m = matrices[0][i]
        matrices[0][i] = matrices[3][i]
        matrices[3][i] = m

    return render(request, 'matrices/matrice_ex6.html', {'matrices': matrices})


def matrice_ex7(request):
    matriz = []
    if request.method == 'POST':
        value = request.POST.get('value').split(',')

        for i in value:
            int_i = int(i)
            if int_i != 0:
                error = 'Plaese write just number 0.'
                return render(request, 'matrices/matrice_ex7.html', {'error': error})

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

    return render(request, 'matrices/matrice_ex7.html', {'matriz': matriz})
    

def matrice_ex8(request):
    matrix = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
    ]

    matriz = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
    ]

    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if c > l:
                cy = matriz[l][c]
                matriz[l][c] = matriz[c][l]
                matriz[c][l] = cy

    return render(request, 'matrices/matrice_ex8.html', {'matriz': matriz, 'matrix': matrix})
    
