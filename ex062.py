idades_digitadas = 0
media_idade = 0
pessoas_maiores21 = 0

while True:
    idade = int(input('Idade: '))
    media_idade += idade
    idades_digitadas += 1
    if idade >= 21:
        pessoas_maiores21 += 1
    while True:
        escolha = input(str(('Deseja continuar? [S / N]: '))).strip().upper()
        if escolha not in 'SN':
            print('Erro! Escolha inválida | Tente novamente!')
        else:
            break
    if escolha == 'N':
        break
media_idade = media_idade / idades_digitadas
print(f'Idades digitadas: {idades_digitadas} | Média de idade: {media_idade:.1f} anos | Pessoas com 21 anos ou mais: {pessoas_maiores21} pessoas.')
