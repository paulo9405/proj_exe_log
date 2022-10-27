from django.shortcuts import render

def home(request):
    return render(request, 'loops/home.html')


def loops_ex22(request):
    valor = 0
    parcelas = None
    juros = 0
    v_parc = 0
    total = 0
    if request.method == 'POST':
        value = request.POST.get('value')
        valor = int(value)

    desconto = (valor / 100) * 20
    avista = valor - desconto


    valor_total = {'total_6':  (valor / 100) * 3 + valor,
                   'total_12': (valor / 100) * 6 + valor,
                   'total_18': (valor / 100) * 9 + valor,
                   'total_24': (valor / 100) * 12 + valor,
                   'total_30': (valor / 100) * 15 + valor,
                   'total_36': (valor / 100) * 18 + valor,
                   'total_42': (valor / 100) * 21 + valor,
                   'total_48': (valor / 100) * 24 + valor,
                   'total_54': (valor / 100) * 27 + valor,
                   'total_60': (valor / 100) * 30 + valor,
                   }

    a = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
    p = ['3%', '6%', '9%', '12%', '15%', '18%', '21%', '24%', '27%', '30%']
    b = []
    d = []

    for v_v in valor_total.values():
        b.append(v_v)

    for x, y in enumerate(b):
        d.append(round(y / a[x], 2))


    parcelas = a
    juros = p
    v_parc = d
    total = b
    return render(request, 'loops/loops_ex22.html', {'parcelas': parcelas,
                                                     'juros': juros,
                                                     'v_parc': v_parc,
                                                     'total': total,
                                                     'avista': avista})

