import random

escolha_usuario = str(input('Pedra, Papel ou Tesoura? ')).capitalize().strip()
escolha_maquina = random.choice(['Pedra', 'Papel', 'Tesoura'])

print(f'Usuário jogou {escolha_usuario} e Computador jogou {escolha_maquina}.')
if escolha_usuario == escolha_maquina:
    print('EMPATE!')
else:
    if (escolha_usuario == 'Pedra' and escolha_maquina == 'Tesoura') or (escolha_usuario == 'Tesoura' and escolha_maquina == 'Papel') or (escolha_usuario == 'Papel' and escolha_maquina == 'Pedra'):
        print('Usuário venceu!')
    else:
        print('Máquina venceu!')
