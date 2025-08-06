-- Problem: Weather Observation Station 4
-- https://www.hackerrank.com/challenges/weather-observation-station-4/problem
-- Descrição:

SELECT COUNT(city) - COUNT(DISTINCT city) AS difference
FROM station
