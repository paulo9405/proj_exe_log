from django.shortcuts import render
from .functions_f import (
    media_student,
    media_ponderada,
    media_harmonica,
    primo,
    calc,
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


