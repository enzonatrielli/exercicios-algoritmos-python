from random import randint

escolha_computador = randint(1, 5)

while True:
    escolha_usuario = int(input('Escolha um número de 1 a 5: '))
    if escolha_usuario not in [1, 2, 3, 4, 5]:
        print('Erro! Escolha Inválida!')
    else:
        if escolha_usuario == escolha_computador:
            print('Você venceu!')
        else:
            print('Você perdeu!')
        break
print(f'Você escolheu {escolha_usuario} e máquina escolheu {escolha_computador}.')
