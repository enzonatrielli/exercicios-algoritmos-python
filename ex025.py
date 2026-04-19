seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))

if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo!')
    