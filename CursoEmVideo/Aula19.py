# AULA 19 

# DICIONÁRIOS: variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

dados = {
    'nome': "Marcelo",
    'idade': 23,
    'peso': 87.5
}
dados['sexo'] = 'Masculino'
print(dados)

del dados['idade']

print(dados)

filme = {
    'TITULO': 'Star Wars',
    'ANO': 1977,
    'DIRETOR': 'Geroge Lucas'
}

""" print(filme.values())
print(filme.keys())
print(filme.items()) """

for k,v in filme.items():
    print(f'O {k} é {v}')

filme2 = {
    'TITULO': 'Avengers',
    'ANO': 2012,
    'DIRETOR': 'Joss Whedon'
}

locadora = [filme, filme2]
print(locadora[1]['TITULO'])

# PARTE PRÁTICA
print('-='*15)

pessoas = {
    'nome': "Marcelo",
    'idade': 23,
    'sexo': 'M',
    'peso': 87.5
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-='*15)

estado = {
    'uf': 'Rio de Janeiro', 
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}

brasil = []
brasil.append(estado)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(f'Brasil: {brasil[0]["uf"]}')
print(brasil[1]['sigla'])

print('-='*15)

estados = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estados.copy())
print(brasil)