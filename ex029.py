nome = str(input('Nome do funcionário: ')).upper()
salario = int(input('Salário (em reais): R$ '))
anos_trabalhados = int(input('Anos trabalhados na empresa: '))
novo_salario = salario + (salario * 0.03)

print(f'Nome: {nome} - Salário atual: R$ {salario:.2f} - Anos trabalhados: {anos_trabalhados} ano(s).')
if anos_trabalhados >= 10:
    novo_salario = salario + (salario * 0.20)
elif anos_trabalhados > 3:
    novo_salario = salario + (salario * 0.125)
print(f'Novo salário: R$ {novo_salario:.2f} ')
