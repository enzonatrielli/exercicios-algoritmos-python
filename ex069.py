primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
soma = 0
pa = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, pa + 1, razao):
    if i == pa:
        print(i, end=' = ')
    else:
        print(i, end=' + ')
    soma += i
print(soma)
