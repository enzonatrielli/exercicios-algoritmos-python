i = 1
pares = 0
impares = 0

while i <= 6:
    numero = int(input(f'[{i}] - Digite um número inteiro: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1
print(f'{pares} pares e {impares} ímpares.')
