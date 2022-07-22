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


def ex4(request):
    vet = []
    vet_list = []
    in_vet = None
    value_x = None
    if request.method == 'POST':
        value = request.POST.get('vector_1')
        vet = value.split(",")
        value_x = request.POST.get('value_x')

        for i in vet:
            c = i.replace(' ', '')
            vet_list.append(c)

    if value_x not in vet_list:
        not_in = 'Value not in vector.'
        return render(request, 'ex4.html', {'not_in': not_in})

    in_vet = vet_list.index(value_x)
    return render(request, 'ex4.html', {'in_vet': in_vet, 'vet_list': vet_list, 'value_x': value_x})