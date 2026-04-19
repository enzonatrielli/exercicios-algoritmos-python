from random import randint

vetor = []

for i in range(10):
    vetor.append(randint(0, 10))
print(vetor)
print('Números pares: ', end='')
for indice, valor in enumerate(vetor):
    if valor % 2 == 0:
        print(f' Posição [{indice}] - Número {valor} |', end=' ')
