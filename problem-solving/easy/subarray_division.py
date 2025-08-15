# Problem: Subarray Division
# Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Descrição: Dada uma lista de inteiros representando os quadrados de uma barra de chocolate,
# # devemos encontrar quantos segmentos contíguos têm soma igual a 'd' e comprimento igual a 'm'.

def birthday(s, d, m):
    cont = 0
    for i in range(len(s) - m + 1):
        soma = sum(s[i:i + m])
        if soma == d:
            cont += 1

    return cont

s = [4]
d = 4
m = 1

print(birthday(s, d, m))