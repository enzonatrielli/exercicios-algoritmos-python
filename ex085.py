nomes = []
sexos = []
salarios = []

for i in range(5):
    nome = str(input('Nome: ')).strip().capitalize()
    sexo = str(input('Sexo [M / F]: ')).upper().strip()
    salario = int(input('Salário: R$ '))
    nomes.append(nome)
    sexos.append(sexo)
    salarios.append(salario)

print('\nMulheres que ganham mais de R$ 5000:\n ')
for k, v in enumerate(salarios):
    if v >= 5000 and sexos[k] == 'F':
        print(f'{nomes[k]} - R$ {v:.2f}', end='\n')
