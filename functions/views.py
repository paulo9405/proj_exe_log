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


def functions_ex12(request):
    res = None
    if request.method == 'POST':
        value1 = request.POST.get('value1').upper()
        value2 = request.POST.get('value2')
        value3 = request.POST.get('value3')

        def weight_ideal(s, a, w):
            s = value1
            a = int(value2) / 100
            w = float(value3)
            if s == 'M':
                ideal = (w * a) - 58
                return 'ideal weight', ideal

            else:
                if s == 'F':
                    ideal = (w * a) - 44.7
                    return 'ideal weight', ideal

        res = weight_ideal(value1, value2, value3)
    return render(request, 'functions/functions_ex12.html', {'res': res})