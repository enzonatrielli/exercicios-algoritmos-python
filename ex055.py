from random import randint

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tentativas = 4

escolha_computador = randint(1, 10)

while True:
    escolha_usuario = int(input('\nEscolha um número de 1 a 10: '))
    if escolha_usuario not in lista_numeros:
        print('Erro! Escolha Inválida!')
    else:
        if escolha_usuario == escolha_computador:
            print(f'Você venceu!')
            break
        else:
            tentativas -= 1
            if tentativas == 0:
                print(f'Você perdeu! - O número sorteado era {escolha_computador}.')
                break
            else:
                print(f'Você errou! - Tentativas restantes: {tentativas}.')
