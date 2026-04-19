def gerador(txt):
    msg = '-' * (2 * len(txt))  + '\n' + txt.center(2 * len(txt)) + '\n' + '-' * (2 * len(txt))
    return msg

texto = str(input('Digite um título: ')).strip()
print(gerador(texto))
