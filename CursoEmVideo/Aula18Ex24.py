# Exercício

# 24 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
dados_aluno = []

while True:
    dados_aluno.append(str(input('Digite o nome do aluno: ')))
    dados_aluno.append(float(input('Nota 1: ')))
    dados_aluno.append(float(input('Nota 2: ')))
    media_aluno = (dados_aluno[1] + dados_aluno[2]) / 2
    dados_aluno.append(media_aluno)
    alunos.append(dados_aluno[:])
    dados_aluno.clear()

    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        for a in alunos:
            print(f'Número do aluno: {alunos.index(a)}     Nome: {a[0]}    Média: {a[3]}')
        """ while True: 
            checar_notasAluno = str(input('Deseja analisar as notas de algum aluno? [S/N]'))
            if checar_notasAluno in 'Ss':
                buscar_aluno = str(input('Qual o nome do aluno? '))
                if buscar_aluno in alunos:
                    print(f'Nota 1: {alunos[1]}   Nota 2: {alunos[2]}')
            else: """
        break
    