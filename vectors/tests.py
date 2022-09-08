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