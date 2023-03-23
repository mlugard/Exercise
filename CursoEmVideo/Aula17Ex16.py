# 16 - Crie um programa que vai ler vários números e colocar numa lista. Depois disso, mostre:
# A) Quantos números foram digitados;
# B) A lista de valores ordenada de forma decrescente;
# C) Se o valor 5 foi digitado ou não está na lista.

numeros = []

while True: 
    n = int(input('Digite um número para adicioná-lo à lista: '))
    numeros.append(n)

    continuar = str(input('Deseja continuar? [S/N] '))[0]
    if continuar in 'Nn':
        print(numeros)
        print(f'Foram adicionados {len(numeros)} números.')
        print(f'Lista em ordem decrescente: {sorted(numeros, reverse=True)}')
        if 5 in numeros:
            print(f'O número 5 aparece na {numeros.index(5)+1}ª posição da lista.')
        else:
            print('Não encontrei o número 5 na lista.')
        break