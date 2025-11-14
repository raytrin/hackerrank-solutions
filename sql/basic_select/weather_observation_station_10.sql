-- Problem: Weather Observation Station 10
-- Link: 

SELECT DISTINCT city
FROM STATION
WHERE city REGEXP '[^aeiou]$';