homens = 0
mulheres = 0
media_total = 0
media_homens = 0
mulheres_maiores = 0
i = 1

while i <= 5:
    idade = int(input(f'[{i}] - Idade: '))
    sexo = str(input(f'[{i}] - Sexo [M/F]: ')).strip().upper()
    media_total += idade
    if sexo == 'M':
        homens += 1
        media_homens += idade
    elif sexo == 'F':
        mulheres += 1
        if idade >= 20:
            mulheres_maiores += 1
    i += 1
media_total = media_total / 5
media_homens = media_homens / homens
print(f'Homens: {homens} - Mulheres: {mulheres} | Média total: {media_total:.1f} anos - Média Homens: {media_homens:.1f} anos | Mulheres maiores de 20 anos: {mulheres_maiores} mulheres.')
