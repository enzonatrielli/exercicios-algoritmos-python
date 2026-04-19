maior_idade = 0
homens = 0
mais_jovemf = 0
media_h = 0

while True:
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    idade = int(input('Idade: '))
    if idade > maior_idade:
        maior_idade = idade
    if sexo == 'M':
        homens += 1
        media_h += idade
    elif sexo == 'F':
        if mais_jovemf == 0:
            mais_jovemf = idade
        elif idade < mais_jovemf:
            mais_jovemf = idade
    escolha_continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if escolha_continuar == 'N':
        break
media_h = media_h / homens
print(f'Maior idade: {maior_idade} anos. | Homens: {homens} | Mulher mais jovem: {mais_jovemf} anos | Média Homens: {media_h:.1f} anos.')
