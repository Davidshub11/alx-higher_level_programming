--Write a script that displays the top 3 of cities temperature during July and August ordered by temperature
SELECT
    state,
    MAX(temperature) AS max_temperature
FROM
    temperatures
GROUP BY
    state
ORDER BY
    state;
