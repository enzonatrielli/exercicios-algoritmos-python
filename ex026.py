n1 = int(input('Número 1 (inteiro): '))
n2 = int(input('Número 2 (inteiro): '))

if n1 != n2:
    if n1 > n2:
        print(f'O primeiro valor é maior.')
    else:
        print(f'O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
