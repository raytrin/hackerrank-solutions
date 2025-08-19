# Problem: Find the Runner-Up Score!
# Link:https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Descrição: Encontrar o segundo maior número numa lista.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    unique = sorted(set(arr), reverse=True)
    print(unique[1])