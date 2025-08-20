# Problem: Sherlock and Array
# Link: https://www.hackerrank.com/challenges/sherlock-and-array/problem
# Descrição: Encontrar um elemento no array cuja soma de todos os elementos anteriores
#seja igual a soma de todos os elementos após. Pivot Indexi
arr = [1, 2, 3]

antes = 0
soma_total = sum(arr)
depois = 0

for i in range(len(arr)):
    depois = soma_total - antes - arr[i]
    if antes == depois:
        print("YES")
        break
    antes += arr[i]
else:
    print("NO")




