def parimpar(numero):
    if numero % 2 == 0:
        msg = f'{numero} é par.'
    else:
        msg = f'{numero} é ímpar.'
    return msg

numero = int(input('Digite um número para verificar se é par ou ímpar: '))
print(parimpar(numero))
