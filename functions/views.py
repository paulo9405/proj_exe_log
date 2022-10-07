from django.shortcuts import render


def home(request):
    return render(request, 'functions/home.html')


def functions_ex1(request):
    return render(request, 'functions/functions_ex1.html')


def functions_ex6(request):
    if request.method == 'POST':
        age = request.POST.get('value1')

        def calc(y):
            y = int(age)
            m = y * 12
            d = m * 30

            return d

        tot_day = calc(int(age))

    return render(request, 'functions/functions_ex6.html', {'age': age, 'tot_day': tot_day})


def functions_ex8(request):
    result = None
    value = None
    if request.method == 'POST':
        value = request.POST.get('value')

        def id_categ(a):
            if a >= 5 and a <= 7:
                return 'Infantil A'

            if a >= 8 and a <= 10:
                return 'Infantil B'

            if a >= 11 and a <= 13:
                return 'Juvenil A'

            if a >= 14 and a <= 17:
                return 'Juvenil A'

            if a > 17:
                return 'Juvenil B'

            else:
                return 'Idade permitida a partir de 5 anos.'

        result = id_categ(int(value))
    return render(request, 'functions/functions_ex8.html', {'result': result, 'value': value})
