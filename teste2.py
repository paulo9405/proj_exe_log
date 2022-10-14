matris = [
    [0,0,0,0,0,], # 0
    [0,0,0,0,0,], # 1
    [0,0,0,0,0,], # 2
    [0,0,0,0,0,], # 3
    [0,0,0,0,0,], # 4
]

# (0,0)
# (1,1)
# (2,2)
# (3,3)
# (4,4)

# (0, 4) linha = 0, coluna 4 >> matris[linha][coluna] = 1
# (1, 4)
# (2, 4)
# (3, 4)
# (4, 4)


def imprimeMatris():
    for linha in matris:
        print(linha)

linha = coluna = 0

for _ in range(0, len(matris)):
    matris[linha][coluna] = 1
    linha += 1
    coluna += 1
imprimeMatris()


# for i in range(0, len(matris)):
#     matris[i][i] = 1
