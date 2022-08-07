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


def matrice_ex5(request):
    if request.method != 'POST':
        return render(request, 'matrices/matrice_ex5.html')

    value = request.POST.get('value1').split(',')

    if len(value) != 5:
        error = 'Plaese write just 10 values.'
        return render(request, 'matrices/matrice_ex5.html', {'error': error})

    integers = [int(x) for x in value]
    valid = [x >= 10 for x in integers]

    if (not all(valid)):
        error = 'Plaese write values grater than 9.'
        return render(request, 'matrices/matrice_ex5.html', {'error': error})

    matrices = []
    for x in integers:
        matrices.append([random.randint(1, x) for _ in range(5)])

    value2 = request.POST.get('value2')
    value2_int = int(value2)

    positions = []
    for i in range(0, len(matrices)):
        for j in range(0, len(matrices)):
            if matrices[i][j] == value2_int:
                position = i, j
                positions.append(position)

    for l in matrices:
        for c in l:
            if value2_int == c:
                return render(request, 'matrices/matrice_ex5.html', {
                    'matrices': matrices, 'positions': positions, 'value2_int': value2_int})

    error2 = 'not in matrice.'
    return render(request, 'matrices/matrice_ex5.html', {'matrices': matrices, 'error2': error2, 'value2_int': value2_int})

