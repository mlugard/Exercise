# Exercício

# 24 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []

while True:
    nomeAluno = (str(input('Digite o nome do aluno: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media_aluno = (nota1 + nota2) / 2

    alunos.append([nomeAluno, [nota1, nota2], media_aluno])

    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-='*30)
print(f'{"Nº: ":<4}{"Nome: ":<15}{"Média":>8}')
print('-'*30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8.2f}')

while True: 
    print('-='*30)
    buscar_aluno = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))      
    if buscar_aluno == 999:
        print('ATÉ BREVE!')
        break
    if buscar_aluno <= len(alunos) - 1:
        print(f'Notas de {alunos[buscar_aluno][0]} são: {alunos[buscar_aluno][1]}')

            
