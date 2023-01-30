# 15 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

def inserirEmOrdem(numeros, indice):
    for i in range(len(numeros)):
        if indice < numeros[i]:
            numeros.insert(i, indice)
            return
    numeros.append(indice)

numeros = []
for i in range(5):
    indice = int(input('Digite um número: '))
    inserirEmOrdem(numeros, indice)

print(f'Lista ordenada: {numeros}')
