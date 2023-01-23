# -------------TUPLAS-------------

# TUPLAS são variáveis compostas e IMUTÁVEIS que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais (indices).
# () = TUPLA
# [] = LISTA
# {} = DICIONÁRIO

lanche = ('Hambúrguer', 'Sushi', 'Pizza', 'Pudim')
print(sorted(lanche))

for comida in range(0, len(lanche)):
    print(f'Vou comer {lanche[comida]}')

""" for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida}') """

print('Que isso, comi demais!')

numPar = (2, 4, 6)
numImp = (1, 3, 5)
c = numImp + numPar
print(c)
print(c.count(2))
print(c.index(4))

pessoa = ('Marcelo', 23, 'M', 91.45)
print(pessoa)
del(pessoa)