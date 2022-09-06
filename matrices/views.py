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

def matrice_ex10(request):
    mat = [[10, 2, 3],
           [4, 5, 6],
           [8, 8, 9]]

    highest = 0
    summ_sec = 0
    diag_pri = []
    diag_sec = []

    n = len(mat)
    for i in range(len(mat)):
        diag_pri.append(mat[i][i])
        if mat[i][i] > highest:
            highest = mat[i][i]
        for j in range(len(mat[i])):
            if i + j == (n - 1):
                diag_sec.append(mat[i][j])
                summ_sec += mat[i][j]
    return render(request, 'matrices/matrice_ex10.html', {'mat': mat,
                                                          'highest': highest,
                                                          'summ_sec': summ_sec})