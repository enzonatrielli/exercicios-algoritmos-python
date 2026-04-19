nomes = []
idades = []

for i in range(9):
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    nomes.append(nome)
    idades.append(idade)

print('Lista de Menores de idade:\n')
for indice, idade in enumerate(idades):
    if idade < 18:
        print(f'{nomes[indice]} - {idade} anos.', end='\n')
