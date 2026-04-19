preco = float(input('Insira o preço do produto (em reais): R$ '))
desconto = 5 / 100
preco_final = preco - (preco * desconto)

print(f'O produto originalmente custava R${preco:.2f}, e passará a custar R${preco_final:.2f} com 5% de desconto.')
