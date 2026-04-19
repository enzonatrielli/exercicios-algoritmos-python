def supersomador(x, y):
    soma = 0
    for numero in range(x, y+1):
        soma += numero
    return soma

n1 = int(input('Primeiro número: '))
n2 = int(input(f'{n1} + '))

print(f'O resultado da soma do intervalo entre {n1} e {n2} é {supersomador(n1, n2)}.')
