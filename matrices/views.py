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
    matrices_1 = []
    matrices_2 = []
    matrice_third = []

    if request.method == 'POST':
        value1 = request.POST.get('value1').split(',')
        value2 = request.POST.get('value2').split(',')
        value3 = request.POST.get('value3').split(',')
        value4 = request.POST.get('value4').split(',')

        value5 = request.POST.get('value5').split(',')
        value6 = request.POST.get('value6').split(',')
        value7 = request.POST.get('value7').split(',')
        value8 = request.POST.get('value8').split(',')

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
                                                         'matrice_third': matrice_third})