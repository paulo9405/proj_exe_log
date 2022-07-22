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


def ex5(request):
    vet = []
    vet_list = []
    tot_par = 0
    par = []
    value = None

    if request.method == 'POST':
        value = request.POST.get('vector_x')
        vet = value.split(",")

    for i in vet:
        vet_list.append(int(i))

    for i in vet_list:
        if i % 2 == 0:
            tot_par += 1
            par.append(i)

    tot_par = tot_par
    return render(request, 'ex5.html', {'tot_par': tot_par, 'value': value, 'par': par})
