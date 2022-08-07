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


def matrice_ex3(request):
    if request.method != 'POST':
        return render(request, 'matrices/matrice_ex3.html')

    value1 = request.POST.get('value1').split(',')
    value2 = request.POST.get('value2').split(',')

    integers_1 = [int(x) for x in value1]
    valid_1 = [x >= 4 for x in integers_1]

    integers_2 = [int(x) for x in value2]
    valid_2 = [x >= 4 for x in integers_2]

    if len(value1) != 4:
        error = 'Plaese write just 4 values.'
        return render(request, 'matrices/matrice_ex3.html', {'error': error})

    if (not all(valid_1)) or (not all(valid_2)):
        error = 'Plaese write values grater than 4.'
        return render(request, 'matrices/matrice_ex3.html', {'error': error})

    matrices_1 = []
    for x in integers_1:
        matrices_1.append([random.randint(1, x) for _ in range(4)])

    matrices_2 = []
    for x in integers_2:
        matrices_2.append([random.randint(1, x) for _ in range(4)])

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
                                                         'matrice_third': matrice_third})