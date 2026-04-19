horas_atividade = int(input('Insira a quantidade de horas praticadas no mês: '))
pontos = 0

if horas_atividade < 10:
    pontos = horas_atividade * 2
elif horas_atividade < 20:
    pontos = horas_atividade * 5
else:
    pontos = horas_atividade * 10
valor = pontos * 0.05
print(f'O valor a ser recebido é de R$ {valor:.2f}.')
