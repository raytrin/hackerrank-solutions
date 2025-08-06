-- Problem: Japanese Citie's name
-- Link: https://www.hackerrank.com/challenges/japanese-cities-name/problem
-- Descrição: Selecionar o nome das cidades japonesas na tabela CITY.

SELECT name
FROM city
WHERE countrycode = "JPN"