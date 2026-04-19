def contador(inicio, fim, incremento):
    for i in range(inicio, fim+incremento, incremento):
        print(i, end=' ')
    print('Acabou!')

inicio = int(input('Ínicio do contador: '))
fim = int(input('Fim do contador: '))
incremento = int(input('Incremento do contador: '))
contador(inicio, fim, incremento)
