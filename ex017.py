velocidade = int(input('Velocidade do carro (em km/h): '))
multa = (velocidade - 80) * 5

if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade e foi multado em R${multa:.2f}.')
else:
    print('Você estava dentro do limite de velocidade.')
