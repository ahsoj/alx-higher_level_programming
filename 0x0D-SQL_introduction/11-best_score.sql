-- list all score records with score >= 10
SELECT score, name
from `second_table`
WHERE score >= 10
ORDER BY score DESC;
