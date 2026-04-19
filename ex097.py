def maior(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    return numeros[-1]

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

print(f'O maior número digitado foi {maior(n1, n2, n3)}.')
