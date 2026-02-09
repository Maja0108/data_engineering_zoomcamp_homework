# Week 3

## Preparation

### External table:

```sql
CREATE OR REPLACE EXTERNAL TABLE `my_project.nyc_taxi.yellow_taxi_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://my-bucket/yellow_taxi/yellow_tripdata_2024-*.parquet']
);

```

### Materialized table:

```sql
CREATE OR REPLACE TABLE `my_project.nyc_taxi.yellow_taxi`
AS
SELECT *
FROM `my_project.nyc_taxi.yellow_taxi_external`;
```

## Question 1

```sql
SELECT COUNT(*) 
FROM `my_project.nyc_taxi.yellow_taxi`;
```

### Question 2

```sql
SELECT COUNT(DISTINCT PULocationID)
FROM `my_project.nyc_taxi.yellow_taxi_external`;
```


```sql
SELECT COUNT(DISTINCT PULocationID)
FROM `my_project.nyc_taxi.yellow_taxi`;
```

### Question 3

```sql
SELECT PULocationID
FROM `my_project.nyc_taxi.yellow_taxi`;
```


```sql
SELECT PULocationID, DOLocationID
FROM `my_project.nyc_taxi.yellow_taxi`;
```

### Question 4

```sql
SELECT COUNT(*)
FROM `my_project.nyc_taxi.yellow_taxi`
WHERE fare_amount = 0;
```

### Question 5

```sql
CREATE OR REPLACE TABLE `my_project.nyc_taxi.yellow_taxi_partitioned`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT *
FROM `my_project.nyc_taxi.yellow_taxi`;

```

### Question 6

```sql
SELECT DISTINCT VendorID
FROM `my_project.nyc_taxi.yellow_taxi`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

```

```sql
SELECT DISTINCT VendorID
FROM `my_project.nyc_taxi.yellow_taxi_partitioned`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

```
