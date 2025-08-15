# Problem: Migratory Birds
# Link: https://www.hackerrank.com/challenges/migratory-birds/problem
# Descrição: Dada uma lista de números de 1 a 5, cada um representando uma espécie de pássaro, deveríamos retornar
# um inteiro que representasse o "pássaro" com maior incidência em um array. Em caso de empate,
# o pássaro representado pelo menor número deveria ser retornado.

from collections import Counter

arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

contagem = Counter(arr)
#print(contagem)

maior = max(contagem.values())
todos = [chave for chave, valor in contagem.items() if valor == maior]
menor = min(todos)

print(menor)