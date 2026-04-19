def potencia(base, expoente):
    return base ** expoente

base = int(input('Base: '))
expoente = int(input('Expoente: '))
print(f'O resultado de {base} elevado a {expoente} é {potencia(base, expoente)}.')
