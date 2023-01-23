#Exercício:
# 1-Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 0, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0
while True:
    num = int(input('Digite um número inteiro (0 para parar): '))
    if num == 0:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é: {soma}.')