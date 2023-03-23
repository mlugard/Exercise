# Exercício

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = {}
ficha_jogadores = []
maior_valor = 0
jogador_vencedor = 0

for j in range (0, 4):
    for p in range (0, 4):
        numeroJogador = j + 1
        jogadores['Número do jogador'] = numeroJogador
    jogadores['Valor do dado'] = randint(1, 6)
    if jogadores['Valor do dado'] > maior_valor:
        maior_valor = jogadores['Valor do dado']
        jogador_vencedor = j + 1
    ficha_jogadores.append(jogadores.copy())

for f in ficha_jogadores:
    for v in f.values():
        print(v, end=' ')
    print()

"""
for c in ficha_jogadores:
    print(f'Jogador {ficha_jogadores[c]["Número do jogador"]}: {ficha_jogadores[c]["Valor do dado"]}') """

print(f'O maior valor tirado foi: {maior_valor}')
print(f'O vencedor foi o jogador {jogador_vencedor}')


