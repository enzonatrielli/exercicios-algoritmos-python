from random import randint

vetor = []

for i in range(7):
    numero = randint(0, 100)
    vetor.append(numero)
    print(f'Número gerado: {vetor[i]}.')
