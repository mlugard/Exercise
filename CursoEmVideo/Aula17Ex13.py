# 13 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posições na lista.


numeros = []
for n in range(0, 5):
    numeros.append(int(input('Digite um número para adicioná-lo à lista: ')))

print(f'Você digitou os valores: {numeros}')
print(f'O maior número da lista é: {max(numeros)}')
print(f'E se encontra na posição: ', end='')
for i, n in enumerate(numeros):
    if n == max(numeros):
        print(f'{i+1}...', end='')
print()
print(f'O menor número da lista é: {min(numeros)}')
print(f'E se encontra na posição: ', end='')
for i, n in enumerate(numeros):
    if n == min(numeros):
        print(f'{i+1}...', end='')

