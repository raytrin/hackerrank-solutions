# Problem: Birthday Cake Candles
# Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Descrição: Conta quantas velas têm a altura máxima.

def birthdayCakeCandles(candles):
    maximo = max(candles)
    cont = 0
    for i in candles:
        if i == maximo:
            cont += 1
    return cont

#exemplo
if __name__ == "__main__":
    candles = [3, 3, 1, 2]
    print(birthdayCakeCandles(candles))
