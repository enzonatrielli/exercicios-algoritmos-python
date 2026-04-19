maior = 0
menor = 0
i = 1

while i <= 8:
    preco = float(input(f'[{i}] - Digite o preço do produto: R$ '))
    if preco > maior:
        maior = preco
    if menor == 0:
        menor = preco
    elif preco < menor:
        menor = preco
    i += 1
print(f'O maior preço foi de R$ {maior:.2f}, e o menor foi de R$ {menor:.2f}.')
