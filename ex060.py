nome_maisvelha = ''
idade_maisvelha = 0
nome_mulherjovem = ''
idade_maisjovemf = 0
media_idade = 0
homens_mais30 = 0
mulheres_menos18 = 0
pessoas = 0

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Nome Pessoa Mais Velha
    if idade > idade_maisvelha:
        idade_maisvelha = idade
        nome_maisvelha = nome

    # Nome Mulher Mais Jovem e Mulheres Menores de 18 anos   
    if sexo == 'F':
        if idade < 18:
            mulheres_menos18 += 1
        if idade_maisjovemf == 0 or idade < idade_maisjovemf:
            idade_maisjovemf = idade
            nome_mulherjovem = nome

    # Homens Maiores de 30 anos
    elif sexo == 'M':
        if idade >= 30:
            homens_mais30 += 1

    # Média Idade        
    media_idade += idade

    # Número de pessoas
    pessoas += 1

    escolha_continuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    if escolha_continuar == 'N':
        break
media_idade = media_idade / pessoas

print(f'Pessoa mais velha: {nome_maisvelha} | Mulher mais jovem: {nome_mulherjovem} | Média de idade: {media_idade:.1f} anos | Homens maiores de 30 anos: {homens_mais30} | Mulheres menores de 18 anos: {mulheres_menos18}.')
