# Problem: Day of the programmer
# Link: https://www.hackerrank.com/challenges/day-of-the-programmer
# Descrição: Retornar a data do dia do programador (256º dia do ano), levando em conta anos bissextos do calendário
# gregoriano e juliano e o ano da transição na Rússia (1918).

ano = 2016
dias = 256

if ano == 1918:
    print(f"26.09.{ano}")
if ano < 1918:
    bissexto = (ano % 4 == 0)
else:
    bissexto = ano % 4 == 0 and (ano % 400 == 0 or not ano % 100 == 0)

dia = 12 if bissexto else 13
print(f"{dia}.09.{ano}")
