# Laços de Repetição: For & While

# For: utilizado quando sabe-se quantos "passos" levará para chegar ao fim
# Ex.: Dê 5 passos.
# While: repetição quando não sabe-se a quantidade de "passos".
# Ex.: Dê passos enquanto não chegar na sala.

# Break: utilizado para quebrar um laço de repetição

cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont +=1
print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
#print('A soma dos números digitados é: {}' .format(s))
print(f'A soma dos números digitados é: {s}')

nome  = 'Marcelo'
idade = 23
print(f'O {nome} tem {idade} anos.')

