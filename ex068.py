mulheres = 0
homens_pesados = 0
media_mulheres = 0
maior_peso_homem = 0

for i in range(1, 9):
    sexo = str(input('Sexo [M / F]: ')).upper().strip()
    peso = int(input('Peso (em kg): '))
    if sexo == 'F':
        mulheres += 1
        media_mulheres += peso
    elif sexo == 'M':
        if peso > maior_peso_homem:
            maior_peso_homem = peso
        if peso >= 100:
            homens_pesados += 1
media_mulheres = media_mulheres / mulheres
print(f'Mulheres cadastradas: {mulheres} | Homens + de 100 kg: {homens_pesados} | Média de peso mulheres: {media_mulheres:.1f} kg | Maior peso homem: {maior_peso_homem} kg.')   