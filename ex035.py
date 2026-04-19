tipo_carro = str(input(('Tipo de carro alugado [Popular ou Luxo]: '))).strip().capitalize()
dias_aluguel = int(input('Dias de aluguel: '))
km_percorridos = int(input('KMs percorridos: '))
carro_popular = dias_aluguel * 90
carro_luxo = dias_aluguel * 150
valor = 0

if tipo_carro == 'Popular':
    if km_percorridos <= 100:
        carro_popular += km_percorridos * 0.20
    else:
        carro_popular += km_percorridos * 0.10
    valor = carro_popular
elif tipo_carro == 'Luxo':
    if km_percorridos <= 200:
        carro_luxo += km_percorridos * 0.30
    else:
        carro_luxo += km_percorridos * 0.25
    valor = carro_luxo
else:
    print('Erro! Tipo de carro inválido!')
print(f'Carro: [{tipo_carro}] - Valor do aluguel: R$ {valor:.2f}.')
