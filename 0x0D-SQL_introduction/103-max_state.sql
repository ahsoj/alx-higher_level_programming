--display the max tempratures of each state
SELECT `state`, MAX(value) AS `max_temp`
FROM `tempratures`
GROUP BY `state`
ORDER BY `state`;
