def fibonacci(valor):
    fibonacci = [0, 1]
    for contador in range(valor - 2):
        numero = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(numero)
    return fibonacci

escolha = int(input('Quantos números da sequência de Fibonacci deseja ver? '))

for numero in fibonacci(escolha):
    print(numero, end=' >> ')
print('FIM!')
