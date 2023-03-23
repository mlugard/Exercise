# Exercício
# 5 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário deseja continuar. No final mostre:
# A) Qual é o total gasto na compra;
# B) Quantos produtos custam mais de R$1000;
# C) Qual é o nome do produto mais barato.

totalGasto = maisDeMil = 0
listaProdutos = []
listaProdutosPreco = []

while True:
    #Adicionar o nome do produto na lista
    nomeProduto = str(input('Digite o nome do produto: '))
    listaProdutos.append(nomeProduto)

    #Adicionar o preço do produto na lista (mesmo indice)
    precoProduto = float(input('Digite o preço do produto: R$'))
    listaProdutosPreco.append(precoProduto)

    totalGasto += precoProduto

    if precoProduto > 1000:
        maisDeMil += 1

    #Associar os indices para buscar o nome do produto
    maisBarato = min(listaProdutosPreco)
    indexDoMaisBarato = listaProdutosPreco.index(maisBarato)

    continuar = str.upper(input('Deseja continuar? (S/N) '))[0]
    if continuar == 'N':
        print(f'O produto mais barato da sua lista é {listaProdutos[indexDoMaisBarato]}') 
        print(f'O total da compra foi: R${totalGasto:.2f} e {maisDeMil} produtos custam mais de R$1000,00.')
        break
