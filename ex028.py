largura = float(input('Largura do terreno (em metros): '))
comprimento = float(input('Comprimento do terreno (em metros): '))
area = largura * comprimento

print(f'Área do terreno: {area:.0f} m².')
if area < 100:
    print('TERRENO POPULAR')
elif area <= 500:
    print('TERRENO MASTER')
else:
    print('TERRENO VIP')
    