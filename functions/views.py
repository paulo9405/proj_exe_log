from django.shortcuts import render


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

            def media_student(v1):
                v1 = value1
                media = 0
                if value2 == 'A':
                    for i in v1:
                        media += int(i) / len(v1)
                        msg = 'student media'
                    return media, msg

                elif value2 == 'P':
                    media = ((int(v1[0]) * 5) + (int(v1[1]) * 3) + (int(v1[2]) * 2)) / (5 + 2 + 3)
                    msg = 'media ponderada'
                    return media, msg

                elif value2 == 'H':
                    def mcm(x, y, i):
                        z = max(x, y, i)
                        while True:
                            if (z % x == 0) and (z % y == 0) and (z % i == 0):
                                return z
                            z += 1

                    mmc = mcm(int(v1[0]), int(v1[1]), int(v1[2]))
                    r = (mmc / int(v1[0]) * 1) + (mmc / int(v1[1]) * 1) + (mmc / int(v1[2]) * 1)
                    r = (3 * mmc) / r
                    msg = 'media harmonizada'
                    return r, msg

            m = media_student(value1)

    return render(request, 'functions/functions_ex2.html', {'m': m, 'value1': value1})
