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

print(filme.values())
print(filme.keys())
print(filme.items())