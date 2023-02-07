# Exercício:

# 19 - Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) Uma listagem com as pessoas mais pesadas;
# C) Uma lista com as pessoas mais leves.

pessoas = []
dados = []

mais_Pesado = []
mais_Leve = []

while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso dessa pessoa:')))
    pessoas.append(dados[:])
    dados.clear

    for p in pessoas:
        if p[1] > pessoas[p]:
            mais_Pesado.append(pessoas[p])
        elif p[1] < pessoas[p]:
            mais_Leve.append(pessoas[p])

    continuar = str(input('Deseja continuar o cadastro? [S/N] '))
    
    if continuar in 'Nn':
        print(f'Foram cadastradas {len(pessoas)+1} pessoas.')
        print(f'A pessoa mais pesada é: {mais_Pesado[0]} com {mais_Pesado[1]}kg.')
        print(f'E a mais leve é: {mais_Leve[0]} com {mais_Leve[1]}kg.')
        break