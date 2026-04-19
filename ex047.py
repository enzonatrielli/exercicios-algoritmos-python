soma = 0

for i in range(500, -1, -1):
    soma += i
    if i != 0:
        print(i, end= ' + ')
    else:
        print(i, end= f' = {soma}.')
