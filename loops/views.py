from django.shortcuts import render

def home(request):
    return render(request, 'loops/home.html')


def loops_ex1(request):
    res = []
    if request.method == 'POST':
        value = request.POST.get('value')
        for c in range(1, 11):
            r = f'{value} X {c} = {int(value) * c}'
            res.append(r)

    return render(request, 'loops/loops_ex1.html', {'res': res})
