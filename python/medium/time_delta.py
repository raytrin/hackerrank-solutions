# Problem: Time Delta
# Link: https://www.hackerrank.com/challenges/python-time-delta/problem
# Descrição: Calcula a diferença absoluta em segundos entre duas datas com timezone.

from datetime import datetime

#datas de exemplo
t1 = 'Sat 02 May 2015 19:54:36 +0530'
t2 = 'Fri 01 May 2015 13:54:36 -0000'

#conversão para datetime com timezone
dat1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
dat2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

#cálculo da diferença em segundos
diferenca = dat1 - dat2
total = abs(diferenca.total_seconds())

print(int(total))