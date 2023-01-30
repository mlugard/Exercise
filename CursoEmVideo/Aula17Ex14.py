# 14 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    n = int(input('Digite um número para adicioná-lo à lista: '))
    if isinstance(n, int):
        if n not in numeros:
            print(f'Número {n} adicionado à lista.')
            numeros.append(n)
            print(numeros)
        else:
            print('Número duplicado, não irei adicionar.')
    else:
        n = int(input('Digite um valor válido para adicioná-lo à lista: '))
        
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        print(f'Os valores digitados (em ordem crescente) foram: {sorted(numeros)}')
        break
    