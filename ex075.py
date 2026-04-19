fibonacci = [0, 1]

for i in range(15):
    numero = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(numero)
print(fibonacci)
