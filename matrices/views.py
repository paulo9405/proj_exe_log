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
