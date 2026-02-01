# Solution of the homeworks

Backfill the data for the question with the material from the class: /flows/05_postgres_taxi_scheduled.yaml

## 1. 
From Kestra UI

## 2. 
Filename also from the UI

## 3.
```sql
SELECT COUNT(*) 
FROM yellow_tripdata
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2020;
```

## 4. 
```sql
SELECT COUNT(*) 
FROM green_tripdata
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2020;
```

## 5.
```sql
SELECT COUNT(*) 
FROM yellow_tripdata
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2021 AND EXTRACT(MONTH FROM tpep_pickup_datetime) = 3 
```

## 6.
timezone = America/New_York
