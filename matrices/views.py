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

    return render(request, 'matrices/matrice_ex1.html', {'matrices': matrices,
                                                         'maior': maior,
                                                         'position': position})


def matrice_ex6(request):
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