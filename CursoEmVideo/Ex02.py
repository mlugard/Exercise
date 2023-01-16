# Exercício:
# 2- Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('Para finalizar insira um valor negativo.')
    if num < 0:
        print('Programa finalizado.')
        break
    for i in table:
        print(num, ' X ', i, ' = ', num * i)