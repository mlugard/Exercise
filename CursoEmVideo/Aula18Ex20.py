# Exercício:

# 20 - Crie um programa que leia onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]
valor = 0

for num in range(0, 7):
    valor = (int(input(f'Digite o {num+1}º número: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
        numeros[0].sort()
    else:
        numeros[1].append(valor)
        numeros[1].sort()

print('-=' * 30)
print(f'Valores pares: {numeros[0]}')
print(f'Valores ímpares: {numeros[1]}')        
