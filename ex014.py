km_percorridos = int(input('Quantidade de quilômetros percorridos: '))
qtd_dias = int(input('Dias de aluguel: '))
preco_total = (qtd_dias * 90) + (0.20 * km_percorridos)

print(f'O preço total a se pagar será de R${preco_total:.2f}.')
