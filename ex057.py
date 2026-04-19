total_homens = 0
total_mulheres = 0

while True:
    salario = int(input('Salário (em reais): '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        total_homens += salario
    elif sexo == 'F':
        total_mulheres += salario
    escolha_continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if escolha_continuar == 'N':
        break
print(f'Total pago aos homens: R$ {total_homens:.2f} | Total pago as mulheres: R$ {total_mulheres:.2f}.')
