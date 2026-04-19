from random import randint

i = 1
maiores = 0
divisiveis = 0

while i <= 20:
    numero = randint(0, 10)
    print(numero, end=' ')
    if numero > 5:
        maiores += 1
    if numero % 3 == 0:
        divisiveis += 1
    i += 1
print(f'\nNúmeros acima de 5: {maiores}.')
print(f'Números divisíveis por 3: {divisiveis}.')
