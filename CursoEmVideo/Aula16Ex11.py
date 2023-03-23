# Exercício
# 11 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (("Produto 1", 15.00), ("Produto 2", 25.00), ("Produto 3", 35.00), ("Produto 4", 45.00))

print("Listagem de preços:")
print("-------------------")

for produto in produtos:
    print("{:<20} R$ {:.2f}".format(produto[0], produto[1]))
