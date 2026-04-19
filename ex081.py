from random import randint

vetor = []
posicoes_maiores25 = []
media_idade = 0
maior_idade = 0
pos_maior_idade = []

for i in range(8):
    vetor.append(randint(1, 100))
    if vetor[i] > maior_idade:
        maior_idade = vetor[i]
    media_idade += vetor[i]

for k, v in enumerate(vetor):
    if v >= 25:
        posicoes_maiores25.append(k)
    if v == maior_idade:
        pos_maior_idade.append(k)
media_idade = media_idade / 8
print(vetor)
print(f'Média de idade: {media_idade:.1f} anos | Posições de maiores de 25: {posicoes_maiores25} | Maior idade: {maior_idade} na(s) posição(es) {pos_maior_idade}.')
