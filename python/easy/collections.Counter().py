# Problem: collections.Counter()
# Link: https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Descrição: Dado um número de sapatos disponíveis em estoque, número de clientes e compras dos modelos
# disponpiveis, é preciso calcular o valor total obtido nas vendas.

from collections import Counter
#
# def shoe_counter(ss, lsv):
#
#     s = ss.split()
#     ssi = []
#     for i in s:
#         ssi.append(int(i))
#
#     shoe_s = Counter(ssi)
#
#     valor_total = 0
#
#     for i in lsv:
#         shoe_size = i[0]
#         shoe_price = i[1]
#
#         if shoe_size in shoe_s:
#             if shoe_s[shoe_size] > 0:
#                 shoe_s[shoe_size] -= 1
#                 valor_total += shoe_price
#
#     return valor_total
#
# if __name__ == '__main__':
#     x = int(input())
#     ss = input()
#     nc = int(input())
#
#     lsv = []
#     for i in range(nc):
#       sv = input()
#       c, v = sv.split()
#       lsv.append([int(c), int(v)])
#
#     total = shoe_counter(ss, lsv)
#     print(total)
#
# ------------------------------------------------------------
_ = input()

estoque = Counter(map(int, input().split()))

clientes = int(input())

faturamento = 0

for _ in range(clientes):
    tamanho, preco = map(int, input().split())

    if estoque[tamanho] > 0:
        estoque[tamanho] -= 1
        faturamento += preco

print(faturamento)