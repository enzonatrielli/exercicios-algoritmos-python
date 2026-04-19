def gerador(txt, qtd):
    msg = '-' * (2 * len(txt))  + '\n' + qtd * (txt.center(2 * len(txt)) + '\n') + '-' * (2 * len(txt))
    return msg

texto = str(input('Digite um título: ')).strip()
quantidade = int(input('Quantidade de vezes a ser exibido: '))
print(gerador(texto, quantidade))
