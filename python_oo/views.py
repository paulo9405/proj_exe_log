from django.shortcuts import render
from .classes import Contador

def home(request):
    return render(request, 'python_oo/home.html')

def python_oo_ex1(request):
    value_incremente = []
    value_zerar = None
    tot = 0

    if request.method == 'POST':
        value_incremente = request.POST.get('value_incrementa').split(',')
        value_zerar = request.POST.get('value_zerar')

    cont = Contador()

    for i in value_incremente:
        tot = cont.incrementar(int(i))

    tot = tot

    if value_zerar:
        return tot.zerar()

    return render(request, 'python_oo/python_oo_ex1.html', {'tot': tot})
