from django.shortcuts import render
from .functions_f import (
    media_student,
    media_ponderada,
    media_harmonica,
    primo,
    calc,
    id_categ,
    media_studant,
    weight_man,
    weight_women,
)


def home(request):
    return render(request, 'functions/home.html')


def functions_ex1(request):
    if request.method == 'POST':
        value = request.POST.get('value')

        def calculate_volume(r):
            r = r
            pi = 3.14
            v = 4 * (r ** 3)
            v = (v / 3) * pi
            return v

    volume = calculate_volume(int(value))
    volume = round(volume, 2)

    return render(request, 'functions/functions_ex1.html', {'volume': volume, 'radius': value})


def functions_ex2(request):
    m = None
    value1 = None
    if request.method == "POST":
        value1 = request.POST.get('value1').split(",")
        value2 = request.POST.get('value2').upper()
        valid_char = 'APH'
        alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

        for i in value1:
            if len(value1) != 3 or i in alpha:
                error_value = 'Plese write just 3 values numbers.'
                return render(request, 'functions/functions_ex2.html', {'error_value': error_value})

            if value2 not in valid_char:
                error = 'Plese write just one value A, P or H.'
                return render(request, 'functions/functions_ex2.html', {'error': error})

            if value2 == 'A':
                m = media_student(value1)

            if value2 == 'P':
                m = media_ponderada(value1)

            if value2 == 'H':
                m = media_harmonica(value1)

    return render(request, 'functions/functions_ex2.html', {'m': m, 'value1': value1})


def functions_ex3(request):
    is_prime = None
    value = None
    if request.method == 'POST':
        value = request.POST.get('value')
        if int(value) < 0:
            error = 'Please write just positive numbers.'
            return render(request, 'functions/functions_ex3.html', {'error': error})
        is_prime = primo(int(value))
    return render(request, 'functions/functions_ex3.html', {'is_prime': is_prime, 'value': value})


def functions_ex6(request):
    age = None
    tot_day = None
    if request.method == 'POST':
        age = request.POST.get('value1')
        tot_day = calc(int(age))
    return render(request, 'functions/functions_ex6.html', {'age': age, 'tot_day': tot_day})


def functions_ex7(request):
    is_perfect = None
    value = None
    if request.method == 'POST':
        value = request.POST.get('value')
        list_div = []
        for i in range(1, int(value)):
            if int(value) % i == 0:
                list_div.append(i)
            if sum(list_div) == int(value):
                is_perfect = True
            else:
                is_perfect = False
    return render(request, 'functions/functions_ex7.html', {'is_perfect': is_perfect, 'value': value})


def functions_ex8(request):
    result = None
    value = None
    if request.method == 'POST':
        value = request.POST.get('value')
        result = id_categ(int(value))
    return render(request, 'functions/functions_ex8.html', {'result': result, 'value': value})


def functions_ex11(request):
    note = []
    media = 0
    media_sum = None
    media_total = None
    if request.method == 'POST':
        notes = request.POST.get('value').split(',')
        for i in notes:
            note.append(int(i))
            media += int(i)
        media_sum = media / len(note)
        media_sum = round(media_sum, 2)
        media_total = media_studant(media_sum)
    return render(request, 'functions/functions_ex11.html', {'media_sum': media_sum, 'media_total': media_total})


def functions_ex12(request):
    result = None
    if request.method == 'POST':
        value1 = request.POST.get('value1').upper()
        value2 = request.POST.get('value2')
        value3 = request.POST.get('value3')
        if value1 == 'M':
            result = weight_man(value2, value3)
        if value1 == 'F':
            result = weight_women(value2, value3)

    return render(request, 'functions/functions_ex12.html', {'result': result})