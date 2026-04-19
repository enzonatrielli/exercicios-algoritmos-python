seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))
tipo_triangulo = ''

if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    print('Os segmentos podem formar um triângulo!')
    if seg3 == seg1 == seg2:
        tipo_triangulo = 'EQUILÁTERO'
    elif (seg3 != seg1 == seg2) or (seg1 != seg2 == seg3) or (seg2 != seg3 == seg1):
        tipo_triangulo = 'ISÓSCELES'
    else:
        tipo_triangulo = 'ESCALENO'
    print(f'Triângulo {tipo_triangulo}.')
else:
    print('Os segmentos não podem formar um triângulo!')
    