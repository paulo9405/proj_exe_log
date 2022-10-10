from django.shortcuts import render


def home(request):
    return render(request, 'functions/home.html')


def functions_ex1(request):
    return render(request, 'functions/functions_ex1.html')


def functions_ex6(request):
    if request.method == 'POST':
        age = request.POST.get('value1')

        def calc(y):
            y = int(age)
            m = y * 12
            d = m * 30

            return d

        tot_day = calc(int(age))

    return render(request, 'functions/functions_ex6.html', {'age': age, 'tot_day': tot_day})

def functions_ex11(request):
    note = []
    media = 0
    media_sum = None
    media_total = None

    if request.method == 'POST':
        notes = request.POST.get('value').split(',')

        for i in notes:
            note.append(int(i))
            media += int(i)

        def media_studant(a):

            if a >= 0 and a <= 4.9:
                return 'D'

            if a >= 5 and a <= 6.9:
                return 'C'

            if a >= 7 and a <= 8.9:
                return 'B'

            if a >= 9 and a <= 10:
                return 'A'

        media_sum = media / len(note)
        media_sum = round(media_sum, 2)
        media_total = media_studant(media_sum)
    return render(request, 'functions/functions_ex11.html', {'media_sum': media_sum, 'media_total': media_total})
