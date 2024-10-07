[![CI](https://github.com/nogibjj/skye-assignment-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/skye-assignment-5/actions/workflows/cicd.yml)
# Skye Assignment 5 - SQL Database Operations
This repository contains a Python script that connects to a SQL database, performs CRUD (Create, Read, Update, Delete) operations, and executes two different SQL queries. Additionally, the project includes a CI/CD pipeline that tests each operation, verifying the correct execution of database operations.

## Logging Details [link](https://github.com/nogibjj/skye-assignment-5/blob/main/log/database_log.log).
- **Log Location**: All logs are saved in the `log` folder. 
- **Log Level**: Database operations are logged at the _debug level_ for detailed traceability.
- **Log Format**: Includes timestamps, log levels, and messages.

## CI/CD Pipeline

A CI/CD pipeline is configured using GitHub Actions to automatically test each database operation. The pipeline loads the `.db` file and runs the operations to ensure they work as expected.

## SQL Queries Used

The following SQL queries are used within the script:

- **Select Query with Condition**: Retrieves a specific record based on `id`.
- **Select All Query**: Retrieves all records from the `transfer` table.
- **Insert Query**: Adds a new record to the `transfer` table.
- **Update Query**: Updates an existing record in the `transfer` table.
- **Delete Query**: Removes a record from the `transfer` table.
