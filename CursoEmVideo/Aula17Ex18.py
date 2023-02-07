# 18 - Crie um programa onde o usuário digite uma expressão qualquer que use *parênteses*.Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

def verifica_expressao(expressao):
  pilha = []
  for char in expressao:
    if char == '(':
      pilha.append(char)
    elif char == ')':
      if not pilha:
        return False
      pilha.pop()
  return not pilha

expressao = input("Digite a expressão: ")
if verifica_expressao(expressao):
  print("A expressão está correta.")
else:
  print("A expressão está incorreta.")

# CORREÇÃO DO PROFESSOR:

expression = str(input('Digite a expressão: '))
pilha = []
for simb in expression:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('Sua expressão está certa.')
else:
  print('Sua expressão está errada.')