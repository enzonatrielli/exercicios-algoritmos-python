from random import randint

vetor = []

for i in range(15):
    vetor.append(randint(0, 100))
print(vetor)
print('Os múltiplos de 10 foram digitados nas posições: ', end='')
for i in range(len(vetor)):
    if vetor[i] % 10 == 0:
        print(i, end=' ')
