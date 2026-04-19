def media(a, b):
    nota_final = (a + b) / 2
    return nota_final

def situacao(nota):
    if nota >= 6:
        return f'APROVADO! Nota {nota:.2f}'
    elif 5 >= nota >= 4:
        return f'RECUPERAÇÃO! Nota {nota:.2f}'
    else:
        return f'REPROVADO! Nota {nota:.2f}'
    
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print(f'Situação do aluno: {situacao(media(n1, n2))}.')
