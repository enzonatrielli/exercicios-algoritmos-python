lista_nomes = []

for i in range(7):
    nome = str(input('Nome: ')).capitalize().strip()
    lista_nomes.append(nome)
print(list(reversed(lista_nomes)))
