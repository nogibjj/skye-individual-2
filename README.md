[![CI](https://github.com/nogibjj/skye-assignment-6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/skye-assignment-6/actions/workflows/cicd.yml)
# Skye Assignment 5 - SQL Database Operations
This repository contains a Python script that connects to a SQL database, performs CRUD (Create, Read, Update, Delete) operations, and executes two different SQL queries. Additionally, the project includes a CI/CD pipeline that tests each operation, verifying the correct execution of database operations.

# SQL Query Explanation
The SQL query provided demonstrates the use of joins, aggregation, and sorting. It operates on a single table, `transfer`, which contains information about player transfers between federations. Below is a breakdown of the query and its purpose.

## Query Breakdown
### WITH Clause: ``latest_transfer_per_federation``
```sql
WITH latest_transfer_per_federation AS (
    SELECT 
        federation, 
        MAX(transfer_date) AS latest_transfer_date
    FROM transfer
    GROUP BY federation
)
```
The `WITH` clause defines a Common Table Expression (CTE) named `latest_transfer_per_federation`, which calculates the most recent transfer date for each federation by:
- Selecting the `federation` column from the transfer table.
- Using `MAX(transfer_date)` to find the most recent date of transfer for each federation.
- Grouping the results by `federation` to ensure we get the latest date for each unique federation.
The result is a temporary table (`latest_transfer_per_federation`) with two columns:
- `federation`: The federation name.
- `latest_transfer_date`: The most recent date of transfer for the federation.

### Main Query: ``Joining the CTE with the transfer Table``
```sql
SELECT 
    l.federation,
    COUNT(t.id) AS transfer_count,
    l.latest_transfer_date
FROM latest_transfer_per_federation l
JOIN transfer t
ON l.federation = t.federation
GROUP BY l.federation, l.latest_transfer_date
ORDER BY l.latest_transfer_date DESC;
```
1. Main Query Selection:
- We select the `federation` from the CTE (`latest_transfer_per_federation`) using the alias `l`.
- We count the total number of transfers for each federation using `COUNT(t.id)` to get the total number of transfers (`transfer_count`).
- We also include `l.latest_transfer_date` to show the most recent transfer date.
2. JOIN Operation:
- The CTE is joined with the original `transfer` table on the `federation` column to count all the transfers associated with each federation.
3. Group By:
- The results are grouped by federation and latest_transfer_date to ensure the correct aggregation is applied.
4. Ordering:
- The results are ordered by latest_transfer_date in descending order, showing the federations with the most recent transfers at the top.

## Initial Data
![insert_data.png](insert_data.png)
## Query Result
![result_of_the_query](query_result.png)

### Final Output
The query produces the following columns in the result set:
- `federation`: The name of the federation.
- `transfer_count`: The total number of transfers for that federation.
- `latest_transfer_date`: The most recent date when a transfer occurred for that federation.

## Logging Details [link](https://github.com/nogibjj/skye-assignment-5/blob/main/log/database_log.log).
- **Log Location**: All logs are saved in the `log` folder. 
- **Log Level**: Database operations are logged at the _debug level_ for detailed traceability.
- **Log Format**: Includes timestamps, log levels, and messages.

## CI/CD Pipeline
A CI/CD pipeline is configured using GitHub Actions to automatically test each database operation. The pipeline loads the `.db` file and runs the operations to ensure they work as expected.
