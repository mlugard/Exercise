# 17 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

while True:
    n = int(input('Digite um número para adicioná-lo à lista: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        print(f'Lista dos números adicionados: {numeros}')
        print(f'Lista dos números pares: {pares}')
        print(f'Lista dos números ímpares: {impares}')
        break
    