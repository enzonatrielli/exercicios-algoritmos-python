alunos = 0
media = 0

while True:
    idade = int(input('Digite a idade do aluno da turma [999 para sair]: '))
    if idade == 999:
        break
    alunos += 1
    media += idade
media = media / alunos
print(f'Alunos: {alunos} alunos | Média de idade: {media:.1f} anos.')
