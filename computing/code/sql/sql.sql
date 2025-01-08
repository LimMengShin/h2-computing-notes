-- SQL SYNTAX

SELECT table1.id, table1.class, SUM(table1.id) AS s FROM table1
INNER JOIN table2 ON table1.id = table2.id
WHERE table1.id > 2
GROUP BY table1.class
HAVING s < 9
ORDER BY table1.id DESC
LIMIT 2;