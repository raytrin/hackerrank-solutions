# Problem: Cats and a mouse
# Link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Descrição: Dois gatos e um rato estão em posições variadas. Devemos determinar qual gato irá
#alcançar o rato primeiro ou se ambos chegarão ao mesmo tempo, fazendo o rato fugir. Para cada
#situação deve ser impresso o nome do vencedor (Cat A, Cat B ou Mouse C).

x = 1
y = 3
z = 2

distancia_cat_a = abs(z - x)
distancia_cat_b = abs(z - y)

if distancia_cat_a < distancia_cat_b:
    print("Cat A")
elif distancia_cat_b < distancia_cat_a:
    print("Cat B")
elif distancia_cat_a == distancia_cat_b:
    print("Mouse C")
