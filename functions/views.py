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