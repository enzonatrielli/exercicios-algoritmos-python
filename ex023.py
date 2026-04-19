nome = str(input('Insira seu nome: ')).upper()
sexo = str(input('Sexo [M/F]: ')).upper()
valor = float(input('Valor das compras (em reais): '))
preco = 0

if sexo == 'M':
    preco = valor - (valor * (5 / 100))
elif sexo == 'F':
    preco = valor - (valor * (13 / 100))
print(f'Cliente: {nome} - Sexo: {sexo} - Valor final da compra: R$ {preco:.2f}.')
