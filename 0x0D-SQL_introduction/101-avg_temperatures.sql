-- display the average temprature
-- by city ordered by temprature
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `tempratures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
