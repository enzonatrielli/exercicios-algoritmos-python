from random import uniform

notas = []
media = 0
alunos_acima = 0
maior_nota = 0
pos_maior_nota = []

for i in range(10):
    notas.append(round(uniform(0, 10), 2))
    media += notas[i]
    if notas[i] > maior_nota:
        maior_nota = notas[i]
    if notas[i] > 6:
        alunos_acima += 1

for k, v in enumerate(notas):
    if v == maior_nota:
        pos_maior_nota.append(k)

media = media / 10
print(notas)
print(f'Média da turma: {media:.1f} | Alunos acima da média: {alunos_acima} | Maior nota: {maior_nota} na(s) posiçõe(s): {pos_maior_nota}.')
