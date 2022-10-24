from django.shortcuts import render

def home(request):
    return render(request, 'loops/home.html')


def loops_ex7(request):
    value = 0
    total_decont = 0
    unidades_de_cem = 0
    total = 0
    if request.method == 'POST':
        value = request.POST.get('value')
        total = int(value)
        resto = total - 500
        unidades_de_100 = resto / 100
        unidades_de_cem = int(unidades_de_100)

    if total < 500:
        v_final = int(value)
        return render(request, 'loops/loops_ex7.html', {'v_final': v_final,
                                                        'total_decont': total_decont,
                                                        'value': value}, )


    while unidades_de_cem <= 25:
        total_decont = (total / 100)
        total_decont = int(total_decont) * unidades_de_cem
        v_final = total - total_decont
        return render(request, 'loops/loops_ex7.html', {'v_final': v_final,
                                                        'total_decont': total_decont,
                                                        'unidades_de_cem': unidades_de_cem,
                                                        'value': value}, )

    else:
        total_decont = total / 4
        total_decont = int(total_decont)
        unidades_de_cem = 25
        v_final = total - total_decont
        return render(request, 'loops/loops_ex7.html', {'v_final': v_final,
                                                        'total_decont': total_decont,
                                                        'unidades_de_cem': unidades_de_cem,
                                                        'value': value}, )


