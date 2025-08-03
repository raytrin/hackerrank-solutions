-- Problem: Revising the Select Query II
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
-- Descrição: Retorna o nome de todas as cidades dos EUA com população maior que 120.000.

SELECT name
FROM city
WHERE countrycode = 'USA'
AND population > 120000