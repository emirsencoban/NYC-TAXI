-- Top 5 pick-up locations with the highest average tip
SELECT PULocationID, AVG(tip_amount) AS average_tip
FROM yellow_tripdata_2025_01
GROUP BY  PULocationID 
ORDER BY average_tip DESC
LIMIT 5;

-- Top 5 drop-off locations with the highest average total amount for trips longer than 5 miles
SELECT DOLocationID , AVG(total_amount) AS average_amount
FROM yellow_tripdata_2025_01
WHERE trip_distance > 5
GROUP BY DOLocationID  
ORDER BY average_amount DESC
LIMIT 5;