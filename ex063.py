soma = 0
menor_valor = 0
numeros = 0
pares = 0
media = 0

while True:
    numero = int(input('Digite um número inteiro: '))
    soma += numero
    numeros += 1
    if menor_valor == 0:
        menor_valor = numero
    elif numero < menor_valor:
        menor_valor = numero
    if numero % 2 == 0:
        pares += 1
    while True:
        escolha = str(input('Deseja continuar? [S / N]: ')).upper().strip()
        if escolha not in ['S', 'N']:
            print('Escolha inválida | Tente novamente!')
        else:
            break
    if escolha == 'N':
        break
media = soma / numeros
print(f'Soma dos valores: {soma} | Menor valor: {menor_valor} | Média: {media:.1f} | Pares: {pares} números.')
    