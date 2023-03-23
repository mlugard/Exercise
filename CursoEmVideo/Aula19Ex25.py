# Exercício

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

ficha_alunos = {}
alunos = []

for c in range(0,3):
    ficha_alunos['Nome '] = str(input('Digite o nome do aluno: '))
    ficha_alunos['Media'] = float(input('Insira a média final do aluno: '))
    if 5.5 < ficha_alunos['Media'] < 7.0:
        ficha_alunos['Situação '] = 'Recuperação'
    elif ficha_alunos['Media'] < 5.5:
        ficha_alunos['Situação '] = 'Reprovado'
    else:
        ficha_alunos['Situação '] = 'Aprovado'
    alunos.append(ficha_alunos.copy())
for f in alunos:
    for v in f.values():
        print(v, end=' ')
    print()