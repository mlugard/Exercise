# Aula 17 - Listas (Parte 1)
# Listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche[3] = 'Picolé'
print(lanche)
lanche.append('Biscoito')
lanche.insert(0, 'Cachorro-quente')
print(lanche)
del lanche[3]
print(lanche)
lanche.pop(0)
print(lanche)

if 'Pizza' in lanche:
    lanche.remove('Pizza')
    print(lanche)

valores = [8,2,5,4,9,3,0]
print(valores)
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)


#---------------PRÁTICA---------------

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 0)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

numeros = []
numeros.append(4)
numeros.append(6)
numeros.append(2)

for c, v in enumerate(numeros):
    print(f'Na posição {c} eu encontrei o valor {v}!')
print('Cheguei ao final da lista!')


a = [2, 3, 4, 5]
b = a[:]
b[2] = 8
print(a)
print(b)