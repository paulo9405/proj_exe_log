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


def ex2(request):
    vet = []
    if request.method == "POST":
        start_vector = int(request.POST.get('value_x'))
        ending_vector = int(request.POST.get('value_y'))
        for i in range(start_vector, ending_vector):
            if i % 2 == 1:
                vet.append(i)
    return render(request, 'ex2.html', {'vet': vet})


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


def ex5(request):
    tot_par = 0
    par = []
    value = []

    if request.method == 'POST':
        value = request.POST.get('vector_x').split(",")

        for i in value:
            i_int = int(i)

            if i_int % 2 == 0:
                tot_par += 1
                par.append(i_int)

    tot_par = tot_par
    return render(request, 'ex5.html', {'tot_par': tot_par, 'value': value, 'par': par})


def ex6(request):
    values = []
    vet_list = []
    if request.method == 'POST':
        values = request.POST.get('value').split(",")

    for index, v in enumerate(values):
        v_int = int(v)
        vet_list.append(int(v))
        if v_int < 0:
            values[index] = '0'

    return render(request, 'ex6.html', {'values': values, 'vet_list': vet_list})


def ex7(request):
    vet_list_1 = []
    vet_list_2 = []
    vet_list_3 = []
    value_1 = []
    value_2 = []

    point_vet1 = 0
    point_vet2 = 0

    if request.method == 'POST':
        value_1 = request.POST.get('value_1').split(",")
        value_2 = request.POST.get('value_2').split(",")

    for i in value_1:
        vet_list_1.append(int(i))

    for i in value_2:
        vet_list_2.append(int(i))

    for i in range(0, len(vet_list_1) + len(vet_list_2)):
        if i % 2 == 0:
            vet_list_3.append(vet_list_1[point_vet1])
            point_vet1 += 1

        else:
            vet_list_3.append(vet_list_2[point_vet2])
            point_vet2 += 1
        # vet_list_3.append(vet_list_1[i])
        # vet_list_3.append(vet_list_2[i])
    return render(request, 'ex7.html', {'vet_list_3': vet_list_3,
                                        'vet_list_1': vet_list_1,
                                        'vet_list_2': vet_list_2})


def ex9(request):
    value = None
    value_without_space = None
    if request.method == "POST":
        value = request.POST.get('value')
        value_without_space = value.replace(" ", "")
    return render(request, 'ex9.html', {'value_without_space': value_without_space,
                                        'value': value})


from num2words import num2words


def ex10(request):
    value = []
    vet_list = []

    if request.method == "POST":
        value = request.POST.get('value').split(",")

        for i in range(0, len(value)):
            vet_list.append(num2words(value[i], lang='en'))

    return render(request, 'ex10.html', {'vet_list': vet_list, 'value': value})


def reversed_string(a_string):
    return a_string[::-1]


def ex11(request):
    value = list
    rever = None
    rev = None
    if request.method == "POST":
        value = request.POST.get('value')

        if reversed_string(value) == value:
            rever = 'É um Anagrama'

        else:
            rev = 'Nao é um Anagrama'
    return render(request, 'ex11.html', {'rever': rever, 'rev': rev, 'value': value})


def ex12(request):
    value1 = []
    value2 = []
    value3 = []
    vet_list1 = []
    vet_list2 = []
    vet_list3 = []
    vet_list = []

    if request.method == 'POST':
        value1 = request.POST.get('value1').split(",")
        value2 = request.POST.get('value2').split(",")
        value3 = request.POST.get('value3').split(",")

    for i in value1:
        vet_list1.append(int(i))

    for i in value2:
        vet_list2.append(int(i))

    for i in value3:
        vet_list3.append(int(i))

    for i in value1:
        vet_list[:3] = value1[:3]

    for i in value2:
        vet_list[3:6] = value2[3:6]

    for i in value3:
        vet_list[6:] = value3[6:]

        if len(vet_list1) + len(vet_list2) + len(vet_list3) != 27:
            erro = 'Plase put just 9 values in each field.'
            return render(request, 'ex12.html', {'erro': erro})
    return render(request, 'ex12.html', {'vet_list': vet_list, 'value1': value1,
                                         'value2': value2, 'value3': value3})
                                         

def ex13(request):
    vet_list = []
    vet = []
    if request.method == 'POST':
        value = request.POST.get('value').split(",")

        for i in value:
            vet_list.append(int(i))

        for i in vet_list:
            if vet_list.count(i) > 1:
                vet.append(i)

    return render(request, 'ex13.html', {'vet_list': vet_list, 'vet': vet})                                        


def ex18(request):
    value = []
    list = []
    list_names = []
    if request.method == 'POST':
        value = request.POST.get('value').split(",")
        list_names = reversed_string(value)

        if len(value) != 5:
            erro = 'Plase write exacly 5 names saparete by comam.'
            return render(request, 'ex18.html', {'erro': erro})
    return render(request, 'ex18.html', {'value': value, 'list_names': list_names})
