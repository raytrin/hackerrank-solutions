-- Problem: Revising the Select Query I
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- Descrição: Retorna todas as colunas das cidades dos EUA com população maior que 100.000.

SELECT *
FROM city
WHERE countrycode = 'USA'
AND population > 100000