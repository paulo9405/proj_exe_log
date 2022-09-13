from django.shortcuts import render


def home(request):
    return render(request, 'functions/home.html')


def functions_ex1(request):
    return render(request, 'functions/functions_ex1.html')

def functions_ex3(request):
    primo_or_not = None
    value = None

    if request.method == 'POST':
        primo_or_not = None
        value = None
        value = request.POST.get('value')

        if int(value) < 0:
            error = 'Please write just positive numbers.'
            return render(request, 'functions/functions_ex3.html', {'error': error})

        def primo(x):
            mult = 0
            for count in range(2, x):
                if (x % count == 0):
                    mult += 1

                if (mult == 0):
                    return True
                return False

        primo_or_not = primo(int(value))

    return render(request, 'functions/functions_ex3.html', {'primo_or_not': primo_or_not, 'value': value})

