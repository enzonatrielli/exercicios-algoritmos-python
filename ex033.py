valor_casa = int(input('Valor da casa (em reais): R$ '))
salario = int(input('Salário do comprador: R$ '))
anos = int(input('Quantidade de anos para pagar: '))
prestacao_mensal = (valor_casa / (anos * 12))

if prestacao_mensal > (salario * 0.3):
    print('Empréstimo Recusado!')
else:
    print('Empréstimo Aprovado!')
print(f'Valor Da Casa: R$ {valor_casa:.2f} - Valor da prestação mensal: R$ {prestacao_mensal:.2f}.')
