# Exercício:

# 20 - Crie um programa que leia onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.

numeros = []
pares = []
impares = []

for num in range(0, 6):
    numeros.append(int(input(f'Digite o {num+1}º número: ')))
    for n in numeros:
        if n % 2 == 0:
            pares.append(n[:])
            pares.sort()
        else:
            impares.append(n[:])
            impares.sort()

print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')        
