from django.shortcuts import render

def home(request):
    return render(request, 'loops/home.html')


def loops_ex7(request):
    value = 0
    total_decont = 0
    unidades_de_cem = 0
    if request.method == 'POST':
        value = request.POST.get('value')

    def desconto(total):
        total = int(value)
        if total < 500:
            valor_final = total
            return valor_final
        resto = total - 500
        unidades_de_cem = resto / 100
        while unidades_de_cem <= 25:
            total_decont = (total / 100) * unidades_de_cem
            valor_final = total - total_decont
            return valor_final
        else:
            total_decont = total / 4
            valor_final = total - total_decont
        return valor_final

    unidades_de_cem = unidades_de_cem
    total_decont = total_decont
    v_final = desconto(int(value))

    return render(request, 'loops/loops_ex7.html', {'v_final': v_final,
                                                    'total_decont': total_decont,
                                                    'unidades_de_cem': unidades_de_cem,
                                                    'value': value},)
