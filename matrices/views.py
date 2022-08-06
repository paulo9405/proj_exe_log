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


import itertools


def matrice_ex2(request):
    if request.method != 'POST':
        return render(request, 'matrices/matrice_ex2.html')

    value1 = request.POST.get('value1').split(',')

    integer1 = [int(x) for x in value1]

    valid_1 = [x == 1 for x in integer1]

    if (not all(valid_1)):
        error = 'Plaese write just 1.'
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
        matrices[linha][coluna] = integer1
        linha += 1
        coluna += 1


    return render(request, 'matrices/matrice_ex2.html',   {'matrices': matrices})
