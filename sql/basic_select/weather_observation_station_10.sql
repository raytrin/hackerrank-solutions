-- Problem: Weather Observation Station 10
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
-- Descrição: Seleciona a o nome da cidade que termine com vogal

SELECT DISTINCT city
FROM STATION
WHERE city REGEXP '[^aeiou]$';