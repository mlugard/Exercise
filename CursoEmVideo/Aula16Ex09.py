# Exercpicio
# 09 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números e também indique o menor e maior valor.

import random

numerosAleatorios = []
contador = 0

while contador <= 5:
    numerosAleatorios.append(random.randint(1, 101)) 
    contador += 1

tuplaAleatoria = (numerosAleatorios)
print(f'Os valores sorteados foram: {tuplaAleatoria}')
print(f'O menor valor é: {min(tuplaAleatoria)}')
print(f'O maior valor é: {max(tuplaAleatoria)}')
