# Exercício
# 3- Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou ao final.

import random

pc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vitorias = 0
soma = 0
resultado = ''

while True:
    escolha = str.upper(input('Você deseja PAR ou IMPAR? '))
    print('Ótimo, vamos jogar!')
    jogador = int(input('Digite seu número inteiro: '))
    numeroPC = random.choice(pc)
    soma = jogador + numeroPC 
    print(f'Você jogou {jogador} e o computador {numeroPC}.')
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    
    if escolha == resultado:
        print('Parabéns! Você ganhou!')
        print('Vamos de novo...')
        vitorias += 1
    else:
        print(f'Poxa, você perdeu... seu total de vitórias foi {vitorias}.')
        print('Até a próxima!')
        break

# Resolução do professor
""" from random import randint
vitoria = 0
while True:
    usuario = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = usuario + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {usuario} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria +=1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria +=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {vitoria} vezes.') """