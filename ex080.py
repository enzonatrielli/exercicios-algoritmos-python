from random import randint

vetor = []
qtd_chave_sorteada = 0
for i in range(30):
    vetor.append(randint(1, 15))

escolha_numero = int(input('Valor a ser encontrado: '))
print(f'O valor {escolha_numero} foi encontrado nas posições: ', end='')
for indice, valor in enumerate(vetor):
    if valor == escolha_numero:
        qtd_chave_sorteada += 1
        print(indice, end=' ')
print(f'\nO valor {escolha_numero} foi sorteado {qtd_chave_sorteada} vez(es).')
