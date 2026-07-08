-- Top 5 pick-up locations with the highest average tip
SELECT PULocationID, AVG(tip_amount) AS average_tip
FROM yellow_tripdata_2025_01
GROUP BY  PULocationID 
ORDER BY average_tip DESC
LIMIT 5;
