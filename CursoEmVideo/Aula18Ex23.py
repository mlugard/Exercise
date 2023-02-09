# Exercício

# 23 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# 1 - Perguntar quantos jogos serão
# 2 - Sortear números e adicionar em uma lista (uma lista para cada jogo)
# 3 - Adicionar as listas de jogo em uma maior contendo todos.

from random import randint

qtd_jogos = int(input('Quantos jogos deseja fazer? '))
jogos = []

palpites_jogos = []

while len(jogos) < qtd_jogos:
    for j in range(0, 6):
        palpites_jogos.append(randint(1, 60))
    jogos.append(palpites_jogos[:])
    palpites_jogos.clear()
print(jogos)


