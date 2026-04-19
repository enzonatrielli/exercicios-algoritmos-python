inicial = int(input('Valor inicial: '))
final = int(input('Valor final: '))
incremento = int(input('Incremento: '))

if inicial > final:
    for i in range(inicial, final-1, incremento):
        print(i, end=' ')
elif inicial == final:
    print('O valor inicial e final são iguais.')
else:
    for i in range(inicial, final+1, incremento):
        print(i, end=' ')
print('Acabou!')
