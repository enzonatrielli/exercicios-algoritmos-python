cigarros_fumados = int(input('Quantos cigarros foram fumados por dia? '))
anos = int(input('Por quantos anos fumou? '))
minutos_perdidos = (cigarros_fumados * (365 * anos)) * 10
dias_perdidos = minutos_perdidos / (60 * 24)

print(f'O fumante já perdeu cerca de {dias_perdidos:.0f} dias de sua vida.')
