def calculate_volume(r):
    r = r
    pi = 3.14
    v = 4 * (r ** 3)
    v = (v / 3) * pi
    return v


def media_student(v1):
    v1 = v1
    media = 0
    for i in v1:
        media += int(i) / len(v1)
        msg = 'student media'
    return media, msg


def media_ponderada(v1):
    v1 = v1
    media = ((int(v1[0]) * 5) + (int(v1[1]) * 3) + (int(v1[2]) * 2)) / (5 + 2 + 3)
    media = round(media, 2)
    msg = 'media ponderada'
    return media, msg


def mcm(x, y, i):
    z = max(x, y, i)
    while True:
        if (z % x == 0) and (z % y == 0) and (z % i == 0):
            return z
        z += 1

def media_harmonica(v1):
        v1 = v1
        mmc = mcm(int(v1[0]), int(v1[1]), int(v1[2]))
        r = (mmc / int(v1[0]) * 1) + (mmc / int(v1[1]) * 1) + (mmc / int(v1[2]) * 1)
        r = round((3 * mmc) / r, 2)
        msg = 'media harmonizada'
        return r, msg


def primo(x):
    mult = 0
    for count in range(2, x):
        if (x % count == 0):
            mult += 1

        if (mult == 0):
            return True
        return False

def calc(y):
    y = y
    m = y * 12
    d = m * 30
    return d


def id_categ(a):
    if a >= 5 and a <= 7:
        return 'Infantil A'
    if a >= 8 and a <= 10:
        return 'Infantil B'
    if a >= 11 and a <= 13:
        return 'Juvenil A'
    if a >= 14 and a <= 17:
        return 'Juvenil A'
    if a > 17:
        return 'Juvenil B'
    else:
        return 'Idade permitida a partir de 5 anos.'


def media_studant(a):
    if a >= 0 and a <= 4.9:
        return 'D'
    if a >= 5 and a <= 6.9:
        return 'C'
    if a >= 7 and a <= 8.9:
        return 'B'
    if a >= 9 and a <= 10:
        return 'A'


def weight_man(a, w):
    a = int(a) / 100
    w = float(w)
    ideal = (w * a) - 58
    return 'ideal weight', ideal


def weight_women(a, w):
    a = int(a) / 100
    w = float(w)
    ideal = (w * a) - 44.7
    return 'ideal weight', ideal