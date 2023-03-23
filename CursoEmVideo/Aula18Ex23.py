# Exercício

# 23 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# 1 - Perguntar quantos jogos serão
# 2 - Sortear números e adicionar em uma lista (uma lista para cada jogo)
# 3 - Adicionar as listas de jogo em uma maior contendo todos.

from random import randint
from time import sleep

print('-='*20)
print('          JOGUE NA MEGA SENA       ')
print('-='*20)

qtd_jogos = int(input('Quantos jogos deseja fazer? '))
jogos = []

palpites_jogo = []

while len(jogos) < qtd_jogos:
    for j in range(0, 6):
        num = randint(1, 60)
        if num not in palpites_jogo:
            palpites_jogo.append(num)
        else:
            num = randint(1, 60)
            palpites_jogo.append(num)
    palpites_jogo.sort()
    jogos.append(palpites_jogo[:])
    palpites_jogo.clear()

print('-=' * 3, f'SORTEANDO {qtd_jogos} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, 'BOA SORTE! ', '-=' * 5)


""" lista = []
jogos = []
print('-' * 30)
print(' JOGA NA MEGA SENA ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, 'BOA SORTE! ', '-=' * 5)"""
