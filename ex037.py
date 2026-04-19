salario = int(input('Insira o salário atual: R$ '))
genero = str(input('Gênero [M / F]: ')).upper().strip()
anos_trabalhados = int(input('Quantidade de anos trabalhados na empresa: '))
salario_novo = salario

if genero == 'M':
    if anos_trabalhados < 20:
        salario_novo += salario * 0.03
    elif anos_trabalhados < 30:
        salario_novo += salario * 0.13
    else:
        salario_novo += salario * 0.25
elif genero == 'F':
    if anos_trabalhados < 15:
        salario_novo += salario * 0.05
    elif anos_trabalhados < 20:
        salario_novo += salario * 0.12
    else:
        salario_novo += salario * 0.23
print(f'O salário passará a ser de R$ {salario_novo:.2f}.')
