def maior(n1, n2):
    if n1 > n2:
        msg = f'{n1} é maior que {n2}.'
    elif n2 > n1:
        msg = f'{n2} é maior que {n1}.'
    else:
        msg = 'Os valores são iguais.'
    return msg

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print(maior(n1, n2))
