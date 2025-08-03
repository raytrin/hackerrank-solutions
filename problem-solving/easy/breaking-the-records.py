# Problem: Breaking the Records
# Link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Descrição: Determinar o número de vezes que o recorde é quebrado para mais e para menos.

#exemplo de scores
scores =  [10, 5, 20, 5, 10]

def breakingRecords(scores):
    score_max = scores[0]
    score_min = scores[0]
    contmax = 0
    contmin = 0

    for i in range(1, len(scores)):
        if scores[i] > score_max:
            score_max = scores[i]
            contmax += 1
        elif scores[i] < score_min:
            score_min = scores[i]
            contmin += 1

    lista = [contmax, contmin]

    return lista