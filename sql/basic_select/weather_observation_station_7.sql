-- Problem: Weather Observation Station 7
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-7/problem
-- Descrição: Selecionar nomes distintos de cidades que terminem com vogais

SELECT DISTINCT city
FROM station
WHERE city LIKE '%a'
or city LIKE '%e'
or city LIKE '%i'
or city LIKE '%o'
or city LIKE '%u';