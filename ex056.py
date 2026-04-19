soma = 0

while True:
    numero = int(input('Digite um número inteiro [1111 para interromper]: '))
    if numero == 1111:
        break
    soma += numero
print(f'Resultado da soma: {soma}.')
