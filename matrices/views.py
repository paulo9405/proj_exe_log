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

