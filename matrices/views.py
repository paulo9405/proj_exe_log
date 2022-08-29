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

def matrice_ex9(request):
    matriz = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
    ]

    matrice = [
        [2, 2, 2, 2, 2],
        [8, 2, 2, 2, 2],
        [8, 8, 2, 2, 2],
        [8, 8, 8, 2, 2],
        [8, 8, 8, 8, 2],
    ]

    for l1 in range(len(matrice)):
        for c1 in range(len(matrice)):
            for l in range(len(matriz)):
                for c in range(len(matriz)):
                    if c > l and l1 > c1:
                        cy = matrice[c1][l1]
                        matrice[c1][l1] = matriz[c][l]
                        matriz[c][l] = cy

    return render(request, 'matrices/matrice_ex9.html', {'matrice': matrice, 'matriz': matriz})