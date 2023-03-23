# Exercício
# 6- Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 30)
print('{:^30}'.format('BANCO CEV'))
print("=" * 30)
saque = int(input('Qual o valor deseja sacar? R$'))
montante = saque
cedulaAtual = 50
totalCedulas = 0
while True:
    if montante >= cedulaAtual:
        montante -= cedulaAtual
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R${cedulaAtual}')
        if cedulaAtual == 50:
            cedulaAtual = 20
        elif cedulaAtual == 20:
            cedulaAtual = 10
        elif cedulaAtual == 10:
            cedulaAtual = 1
        totalCedulas = 0
        if montante == 0:
            break