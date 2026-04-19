soma = 0

for i in range(6, 101):
    soma += i
    if i != 100:
        print(i, end=' + ')
    else:
        print(i, end=f' = {soma}.')
