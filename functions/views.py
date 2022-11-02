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

def functions_ex7(request):
    true_false = None
    value = None
    if request.method == 'POST':
        value = request.POST.get('value')
        list_div = []
        for i in range(1, int(value)):
            if int(value) % i == 0:
                list_div.append(i)
            if sum(list_div) == int(value):
                true_false = True
            else:
                true_false = False
    return render(request, 'functions/functions_ex7.html', {'true_false': true_false, 'value': value})