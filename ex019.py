n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'APROVADO! Média: {media:.2f}.')
else:
    print(f'REPROVADO! Média: {media:.2f}.')
