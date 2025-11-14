-- Problem: Weather Observation Station
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-8/problem
-- Descrição: Seleciona os nomes das cidades que possuem vogais tanto no início
-- quanto no fim.

SELECT DISTINCT city
FROM STATION
WHERE city REGEXP '^[aeiou].*[aeiou]$'; -- ^: início da str
                                        -- .*: representa 0 ou mais char, exceto quebra de linha
                                        -- $: fim da str