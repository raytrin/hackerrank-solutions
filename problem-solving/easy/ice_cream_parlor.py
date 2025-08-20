# Problem: Ice Cream Parlor
# Link: https://www.hackerrank.com/challenges/icecream-parlor/problem
# Descrição: Dado um número (m) precisamos encontrar, em um array, dois números que somados
#dão o número (m) e retornar os seus respectivos índices, usando indexação de base 1.

arr = [2, 2,4, 3]
m = 4

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == m:
            r = (i, j)

print(r[0] + 1, r[1] + 1)

# ----------------------------------------- outra forma mais eficiente de resolver -------------------------------------
# verifica a lista só uma vez e por isso é mai eficiente

arr = [2, 2,4, 3]
m = 6

di = {}
for i, valor in enumerate(arr):
    if m - valor in di:
        print(di[m - valor], i + 1)
    di[valor] = i + 1
