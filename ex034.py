peso = int(input('Insira o peso (em kg): '))
altura = float(input('Insira a altura (em metros): '))
imc = peso / (altura*altura)
faixa = ''

if imc < 18.5:
    faixa = 'Abaixo do Peso'
elif imc < 25:
    faixa = 'Peso ideal'
elif imc < 30:
    faixa = 'Sobrepeso'
elif imc < 40:
    faixa = 'Obesidade'
else:
    faixa = 'Obesidade mórbida'
print(f'Seu IMC é {imc:.1f}, e portanto sua faixa é {faixa}.')
