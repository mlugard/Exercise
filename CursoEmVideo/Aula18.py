# Aula 18 - Listas (parte 2)

# Lista Composta

pessoas = [['Marcelo', 23], ['Giovanna', 20], ['Pedro', 25]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])

# PARTE PRÁTICA

turma = [['Vitor', 21], ['Andre', 20], ['Paulo', 22], ['Musta', 21]]
for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = []
dados = []

total_Maioridade = total_Menores = 0

for c in range (0,3):
    dados.append(str(input('Nome: ')))
    dados.append(str(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        total_Maioridade += 1
    else:
        print(f'{p[0]} é menor de diade.')
        total_Menores += 1
print(f'Temos {total_Maioridade} maiores de idade e {total_Menores} menores de idade.')