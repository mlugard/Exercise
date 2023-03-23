# Exercício
# 07 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

numUsuario = int(input('Digite um número inteiro (0-20):'))
while numUsuario > 20 or numUsuario < 0:
    numUsuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Seu número por extenso: {numeros[numUsuario]}')