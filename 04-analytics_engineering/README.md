# SQL queries for the questions
## Question 3
```sql 
SELECT count(*) FROM fct_monthly_zone_revenue;
```

## Question 4
```sql 
SELECT pickup_zone
FROM fct_monthly_zone_revenue
WHERE revenue_month > '2019-12-01'
  AND service_type = 'Green'
ORDER BY revenue_monthly_total_amount DESC
LIMIT 1;
```
## Question 5
```sql 
SELECT sum(total_monthly_trips) from fct_monthly_zone_revenue where service_type = 'Green' and revenue_month = '2019-10-01';
```
## Question 6
after creating the new dataset (modifying schema.yml, sources.yml), adding stg_fhv_tripdata.sql, then running
```bash
dbt run --select stg_fhv_tripdata --target prod
``` 
query: 
```sql 
select count(*) from stg_fhv_tripdata
```
