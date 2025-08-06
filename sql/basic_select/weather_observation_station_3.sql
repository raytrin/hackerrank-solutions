-- Problem: Weather Observation Station 3
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-3/problem
-- Descrição: Selecionar todas as CIDADES da tabela STATION cujo número de ID sejam pares.

SELECT DISTINCT city
FROM station
WHERE id % 2 = 0


