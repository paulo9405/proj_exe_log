from django.shortcuts import render


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
