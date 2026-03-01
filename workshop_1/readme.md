SELECT MIN(tpep_pickup_datetime), MAX(tpep_pickup_datetime) FROM taxi_data.rides;

SELECT 
    (CAST(COUNT(CASE WHEN payment_type = 1 THEN 1 END) AS FLOAT) / COUNT(*)) * 100 
FROM taxi_data.rides;

SELECT SUM(tip_amount) FROM taxi_data.rides;
