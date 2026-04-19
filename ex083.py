from random import randint

numeros = []

for i in range(20):
    numeros.append(randint(0, 99))

print(numeros)
numeros.sort()
print(f'Valores ordenados: {numeros}')
