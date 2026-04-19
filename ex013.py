salario = float(input('Insira o salário do funcionário (em reais): R$ '))
aumento = 15 / 100
salario_final = salario + (salario * aumento)

print(f'O salário de R${salario:.2f} do funcionário passará a ser de R${salario_final:.2f} com o aumento de 15%.')
