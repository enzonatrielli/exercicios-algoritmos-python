from datetime import datetime

ano_nascimento = int(input('Insira o ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
anos_restantes = 18 - idade
anos_excedidos = idade - 18

if idade < 18:
    print(f'Você deverá se alistar SOMENTE daqui a {anos_restantes} ano(s).')
else:
    print(f'Você deveria ter se alistado faz {anos_excedidos} anos.')
