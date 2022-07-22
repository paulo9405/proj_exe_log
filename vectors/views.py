from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def ex1(request):
    list_value = None
    x = None
    y = None
    x_p = None
    y_p = None
    sum = None

    if request.method == "POST":
        value_1 = request.POST.get('value_1')
        list_value = value_1.split(",")

        x = int(request.POST.get('value_x'))
        y = int(request.POST.get('value_y'))

        x_p = list_value[x]
        y_p = list_value[y]
        sum = int(list_value[x]) + int(list_value[y])

    return render(request, 'ex1.html', {'list_value': list_value,
                                        'x': x, 'y': y, 'x_p': x_p,
                                        'y_p': y_p, 'sum': sum})


def ex3(request):
    vet = []
    a = None
    if request.method == 'POST':
        value_1 = request.POST.get('value_x')
        vet = value_1.split(",")
        div = int(len(vet) / 2)
        a = [vet[div:], vet[:div]]
        if len(vet) > 4 or len(vet) < 4:
            erro = 'Plase write exactly 4 values separated by comma.'
            return render(request, 'ex3.html', {'erro': erro})
    return render(request, 'ex3.html', {'vet': vet, 'a': a})