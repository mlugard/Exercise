# Exercício:

# 19 - Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) Uma listagem com as pessoas mais pesadas;
# C) Uma lista com as pessoas mais leves.

pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break

print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas na lista.')
print(f'O maior peso foi de {maior} kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]')

print(f'O menor peso foi de {menor} kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]')
