# Exercício
# 10 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os numa tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9;
# B) Em que posição foi digitado o primeiro valor 3;
# C) Quais foram os números pares.

listaValores = []
numerosPares = []
contador = 0
posicao = 0

valorDesejado = int(input('Selecione um valor para encontrar: '))
while contador <= 3:
    valor = int(input('Digite um valor: '))
    listaValores.append(valor)
    if valor % 2 == 0:
        numerosPares.append(valor)
    contador += 1

minha_tupla = tuple(listaValores)

print(minha_tupla)

try:
    posicao = minha_tupla.index(valorDesejado) + 1
    print(f'O {valorDesejado} apareceu pela primeira vez na {posicao}ª posição')
except ValueError:
    print(f'{valorDesejado} não foi encontrado na tupla.')

print(f'O número 9 aparece {minha_tupla.count(9)} vez(es).')
print(f'Os números pares digitados foram: {numerosPares}')

