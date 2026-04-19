def media(a, b):
    nota = (a + b) / 2
    return nota

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print(f'A média do aluno é de {media(n1, n2):.2f}.')
