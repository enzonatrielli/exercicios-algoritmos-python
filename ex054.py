media_altura = 0
grupo1 = 0
grupo2 = 0
grupo3 = 0
i = 1

while i <= 7:
    peso = float(input(f'[{i}] - Peso (em kg): '))
    altura = float(input(f'[{i}] - Altura (em metros): '))
    media_altura += altura
    if peso > 90:
        grupo1 += 1
    if peso < 50 and altura < 1.60:
        grupo2 += 1
    elif peso > 100 and altura > 1.90:
        grupo3 += 1
    i += 1
media_altura = media_altura / 7
print(f'Média altura: {media_altura:.2f} metros | Pesam mais de 90kg: {grupo1} | Pesam menos de 50kg e menos de 1.60m: {grupo2} | Medem mais de 1.90m e mais de 100kg: {grupo3}.')
