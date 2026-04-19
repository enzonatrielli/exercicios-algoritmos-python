def gerador(txt, qtd, borda):
    if borda == 1:
        borda = '+-------=======------+'
    elif borda == 2:
        borda = '~~~~~~~~:::::::~~~~~~~'
    elif borda == 3:
        borda = '<<<<<<<<------->>>>>>>'
    else:
        borda = '-' * 20
    if len(txt) > len(borda):
        borda = borda * (len(txt) // 10)
    msg = borda + '\n' + qtd * (txt.center(len(borda)) + '\n') + borda
    return msg

texto = str(input('Digite um título: ')).strip()
quantidade = int(input('Quantidade de vezes a ser exibido: '))
borda = int(input('Bordas\n[1] - +-------=======------+\n[2] - ~~~~~~~~:::::::~~~~~~~\n[3] - <<<<<<<<------->>>>>>>\nOpção desejada: '))
print(gerador(texto, quantidade, borda))
