# Write your MySQL query statement below
SELECT player_id, event_date as first_login
FROM (
    SELECT 
        player_id,
        event_date,
        RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
    FROM Activity
) t
WHERE rn < 2;
