-- Problem: Weather Observation Station 5
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-5/problem
-- Descrição: Mostrar, usando uma consulta SQL, as duas cidades com o nome mais curto e mais longo da tabela, junto com o tamanho desses nomes. Se houver empate, escolher a cidade que vem primeiro em ordem alfabética.

(SELECT city, LENGTH(city) AS shortest_name
FROM station
ORDER BY shortest_name ASC, city ASC
LIMIT 1
)
UNION ALL
(
SELECT city, LENGTH(city) AS longest_name
FROM station
ORDER BY longest_name DESC, city ASC
LIMIT 1
)