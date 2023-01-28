# Exercício
# 12 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'curso', 'programar', 'python', 'linguagem', 'estudar', 'praticar', 'trabalhar', 'programador', 'futuro')

for p in palavras:
    print(f'Na palavra {p.upper()} temos ', end='\n')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='\n')