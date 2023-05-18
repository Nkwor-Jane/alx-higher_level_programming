-- display average temperature
SELECT city,
AVG(value) As 'Average temperature'
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
