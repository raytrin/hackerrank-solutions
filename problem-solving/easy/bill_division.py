# Problem: Bill Division
# Link: https://www.hackerrank.com/challenges/bon-appetit/problem
# Descrição: Verificar se a divisão da conta entre dois amigos está correta, considerando que um deles não comeu um dos itens. Se ele pagou a mais, informar quanto deve ser reembolsado.

#exemplos de valores
bill = [3, 10, 2, 9]
k = 1
b = 12


def bonAppetit(bill, k, b):

    removido = bill.pop(k)
    soma = sum(bill)

    result = soma / 2
    if result == b:
        print("Bon Appetit")
    else:
        print(removido // 2)

bonAppetit(bill, k, b)
