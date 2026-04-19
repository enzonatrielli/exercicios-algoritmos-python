dias_trabalhados = int(input('Quantos dias foram trabalhados no mês? '))
horas_trabalhadas = (8 * dias_trabalhados)
salario = horas_trabalhadas * 25

print(f'O funcionário receberá cerca de R${salario:.2f}.')
