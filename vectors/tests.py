<<<<<<< HEAD
texto = ' abd012'

produtos = ['ABC123', ' abd012', 'ABS111', 'abB222']

def trattar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

# texto = ' abd012'

texto = trattar_texto(texto)

print(texto)

for i, produto in enumerate(produtos):
    produtos[i] = trattar_texto(produto)

print(produtos)


a = 11

def primo(x):
    mult = 0
    for count in range(2, x):
        if (x % count == 0):
            mult += 1

        if (mult == 0):
            return True
        return False

a = primo(a)
print(a)
=======
>>>>>>> 88525b57a7ee0f5574885faa9149ea7fed04cfb7
