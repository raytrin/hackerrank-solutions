# Problem: List Comprehensions
# Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Descrição: Imprimir, usando list comprehension, todas as combinações possíveis de três inteiros dentro de certos limites, cuja soma não seja igual a um número dado.
x = 3
y = 2
z = 1
n = 5

#lista = []
#for i in range(x + 1):
#    for j in range(y + 1):
#        for k in range(z + 1):
#            if i + j + k != n:
#               lista.append([i, j, k])

lista = [[i, j, k] for i in range(x +1) for j in range(y + 1) for k in range(z + 1)  if i + j + k != n]

print(lista)