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

def functions_ex9_ex10(request):
    r1 = None
    r2 = None
    if request.method == 'POST':
        value = request.POST.get('value')

        def neg_pos(a):
            if a >= 0:
                return True
            return False

        def inp_par(a):
            if a % 2 == 0:
                return True
            return False

        r1 = neg_pos(int(value))
        r2 = inp_par(int(value))

    return render(request, 'functions/functions_ex9_ex10.html', {'r1': r1, 'r2': r2})