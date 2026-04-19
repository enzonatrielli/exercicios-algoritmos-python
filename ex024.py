distancia = int(input('Distância a ser percorrida (em km): '))
preco = 0

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem é de R$ {preco:.2f}.')
