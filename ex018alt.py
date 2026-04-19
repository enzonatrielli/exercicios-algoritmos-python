from datetime import datetime

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade < 16:
    print(f'Você não pode votar ainda, pois tem {idade} anos.')
elif 70 <= idade >= 16:
    print(f'Você pode votar OPCIONALMENTE, pois tem {idade} anos.')
else:
    print(f'Você deve OBRIGATORIAMENTE votar, pois tem {idade} anos.')
