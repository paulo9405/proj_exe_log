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