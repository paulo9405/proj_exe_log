from django.shortcuts import render
from .functions_f import media_student, media_ponderada, mcm, media_harmonica


def home(request):
    return render(request, 'functions/home.html')


def functions_ex1(request):
    return render(request, 'functions/functions_ex1.html')


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
