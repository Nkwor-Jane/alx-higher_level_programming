-- list number of record  with same score of table
SELECT `score`,
COUNT(*) AS `number` 
FROM `second_table` 
GROUP BY `score` 
ORDER BY `number` DESC;
