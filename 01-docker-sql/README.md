# Solutions

Tables: 
        - November 2025 data: green_taxi_trips
        - zones and boroughs: taxi_zone_lookup
## Question 1

```bash
docker run -it --entrypoint /bin/bash python:3.13
pip -- version ```


## Question 3
```sql
SELECT
    COUNT(*)
FROM
    green_taxi_trips
WHERE
    trip_distance <= 1.0
AND lpep_pickup_datetime >= '2025-11-01 00:00:00' AND lpep_pickup_datetime < '2025-12-01 00:00:00'; ```

## Question 4
```sql
SELECT
    MaAX(trip_distance), lpep_pickup_datetime
FROM
    green_taxi_trips
WHERE
    trip_distance <= 100
AND lpep_pickup_datetime >= '2025-11-01 00:00:00' AND lpep_pickup_datetime < '2025-12-01 00:00:00'
GROUP BY lpep_pickup_datetime  ORDER BY MAX(trip_distance) DESC LIMIT 1; ```

## Question 5
```sql
SELECT SUM(trip_distance) as total_amount, "PULocationID", t."Zone"
FROM green_taxi_trips g
JOIN taxi_zone_lookup t on g."PULocationID" = t."LocationID" 
WHERE lpep_pickup_datetime >= '2025-11-18 00:00:00' AND lpep_pickup_datetime < '2025-11-19 00:00:00'
GROUP BY "PULocationID", t."Zone" ORDER BY total_amount DESC LIMIT 1; ```

## Question 6
```sql
SELECT
    zdo."Zone" AS dropoff_zone,
    MAX(t.tip_amount) AS max_tip
FROM 
    green_taxi_trips t
JOIN taxi_zone_lookup zpu ON t."PULocationID" = zpu."LocationID"
JOIN taxi_zone_lookup zdo ON t."DOLocationID" = zdo."LocationID"
WHERE
    zpu."Zone" = 'East Harlem North'
    AND t.lpep_pickup_datetime >= '2025-11-01 00:00:00'
    AND t.lpep_pickup_datetime < '2025-12-01 00:00:00'
GROUP BY
    dropoff_zone
ORDER BY
    max_tip DESC
LIMIT 1; ```
