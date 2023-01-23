# Exercício
# 08 - Crie uma tupla com os 20 primeiros colocados na Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados;
# B) Os últimos 4 colocados;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição na tabela está o Corinthians.

linha = '=' * 50
titulo = 'CLASSIFICAÇÃO BRASILEIRÃO 2012'

print(linha)
print(titulo.center(50))
print(linha)

tabelaClassificacao = ('Fluminense', 'Atlético-MG', 'Grêmio', 'São Paulo', 'Vasco da Gama', 'Corinthians', 'Botafogo', 'Santos', 'Cruzeiro', 'Internacional', 'Flamengo', 'Náutico', 'Coritiba', 'Ponte Preta', 'Bahia', 'Portuguesa', 'Sport Recife', 'Palmeiras', 'Atlético-GO', 'Figueirense')
posicaoCorinthians = tabelaClassificacao.index('Corinthians') + 1

print(linha)
print(f'Os 5 primeiros colocados foram: {tabelaClassificacao[0:5]}')
print(linha)
print(f'Tabela em ordem alfabética: {sorted(tabelaClassificacao)}')
print(linha)
print(f'Os 4 últimos colocados foram: {tabelaClassificacao[-4:]}')
print(linha)
print(f'O Corinthians terminou o campeonato em: {posicaoCorinthians}º')