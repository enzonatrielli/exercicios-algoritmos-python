def gerador():
    txt = 'Olá, Mundo!'
    msg = '-' * 20 + '\n' + txt.center(20) + '\n' + '-' * 20
    return msg

print(gerador())
