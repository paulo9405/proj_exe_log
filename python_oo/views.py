from django.shortcuts import render
from .classes import Contador, Person


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


def python_oo_ex9(request):
    dad = None
    mom = None
    son = None
    same_person = None
    brother = None

    if request.method == 'POST':
        dad = request.POST.get('dad')
        mom = request.POST.get('mom')
        son = request.POST.get('son')
        same_person = request.POST.get('same_person')
        brother = request.POST.get('brother')

    dad1 = Person(dad, None, None)
    mom1 = Person(mom, None, None)
    son1 = Person(son, dad, mom)
    same_person1 = Person(son, dad, mom)
    brother1 = Person(brother, dad, mom)
    predecessor = dad1.is_predecessor(son1)
    same = son1.is_same(same_person1)
    subling = son1.is_sibling(brother1)

    return render(request, 'python_oo/python_oo_ex9.html', {'dad': dad,
                                                            'mom': mom,
                                                            'son': son,
                                                            'same_person': same_person,
                                                            'brother': brother,
                                                            'dad1': dad1,
                                                            'mom1': mom1,
                                                            'son1': son1,
                                                            'same_person1': same_person1,
                                                            'subling': subling,
                                                            'predecessor': predecessor,
                                                            'same': same})
