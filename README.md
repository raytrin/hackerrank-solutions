# 🚀 HackerRank Solutions

Repositório com as minhas soluções para os desafios do [HackerRank](https://www.hackerrank.com/), organizadas por linguagem e nível de dificuldade.  
O objetivo é praticar **Python**, **SQL** e **Problem Solving**.

---

## 🌐 Meu Perfil no HackerRank
[![HackerRank Badge](https://img.shields.io/badge/HackerRank-Profile-2EC866?logo=HackerRank&logoColor=white)](https://www.hackerrank.com/rayytrindade)

---

## 📂 Estrutura do Repositório

hackerrank-solutions/
│
├── python/
│ ├── easy/
│ ├── medium/
│
├── problem-solving/
│ ├── easy/
│ ├── medium/
│
└── sql/
├── basic_select/

---

## 🏅 Badges HackerRank
[![Python](https://img.shields.io/badge/Python-5%20Stars-2EC866?logo=HackerRank&logoColor=white)](https://www.hackerrank.com/rayytrindade)
[![Problem Solving](https://img.shields.io/badge/Problem%20Solving-2%20Stars-2EC866?logo=HackerRank&logoColor=white)](https://www.hackerrank.com/rayytrindade)

---

## 📌 Exemplo de Desafio (Python - medium)

```python
# Problem: Time Delta
# Link: https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime

t1 = 'Sat 02 May 2015 19:54:36 +0530'
t2 = 'Fri 01 May 2015 13:54:36 -0000'

dat1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
dat2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

diferenca = dat1 - dat2
total = abs(diferenca.total_seconds())

print(int(total))
```

---

## 📌 Exemplo de Desafio (Problem Solving - easy)
```python
# Problem: Birthday Cake Candles
# Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    maximo = max(candles)
    cont = 0
    for i in candles:
        if i == maximo:
            cont += 1
    return cont

```
---

## 📌 Exemplo de Desafio (SQL - basic select)
```sql
-- Problem: Revising the Select Query I
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem

SELECT *
FROM city
WHERE countrycode = 'USA'
AND population > 100000

```
