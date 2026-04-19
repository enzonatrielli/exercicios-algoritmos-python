media = 0
maiores = 0
menores = 0
maior_idade = 0
i = 1

while i <= 10:
    idade = int(input(f'[{i}] - Insira a idade: '))
    media += idade
    if idade > maior_idade:
        maior_idade = idade
    if idade >= 18:
        maiores += 1
    elif idade <= 5:
        menores += 1
    i += 1
media = media / 10
print(f'Média de idade: {media:.1f} anos - Maiores de 18 anos: {maiores} pessoas - Menores de 5 anos: {menores} pessoas - Maior idade: {maior_idade} anos.')