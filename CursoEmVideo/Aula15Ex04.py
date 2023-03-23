# Exercício
# 4 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não. No final mostre:
# A) Quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados;
# C) Quantas mulheres tem mais de 20 anos.

pessoa = homem = mulher = 0

while True:
    nome = str.upper(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade: '))
    sexo = str.upper(input('Qual é o gênero (H/M)? '))
    if idade > 18:
        pessoa += 1
    if sexo == 'H':
        homem += 1
    if sexo == 'M' and idade < 20:
        mulher += 1
    continueCadastro = str.upper(input('Deseja continuar (S/N)?'))
    if continueCadastro == 'N':
        print(f'Pessoas cadatradas: {pessoa} \n Homens cadastrados: {homem}\n Mulheres cadastradas:{mulher}')
        break

# Resolução do professor

pessoas = homens = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Sexo: [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pessoas}')

