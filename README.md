[![CI](https://github.com/nogibjj/skye-individual-2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/skye-individual-2/actions/workflows/cicd.yml)
# Rust ETL and CRUD CLI Program

This project is a Rust-based CLI program that performs an ETL (Extract, Transform, Load) process on a CSV file and enables CRUD (Create, Read, Update, Delete) operations on the loaded data. The CLI is modular, allowing users to interact with a local SQLite database that stores data about chess player transfers.

## Table of Contents
- [Dependencies](#dependencies)
- [Project Overview](#project-overview)
- [How to Run the Program](#how-to-run-the-program)
- [GitHub Copilot Usage](#github-copilot-usage)
- [LLM Usage](#llm-usage)

## Dependencies
This project uses several Rust crates to handle the CLI, database operations, and CSV data handling. Here’s a breakdown of the dependencies and how to install them:

- **rusqlite**: Provides SQLite bindings to interact with the local SQLite database.
- **structopt**: Parses command-line arguments, making the CLI flexible and user-friendly.
- **reqwest**: Allows HTTP requests, necessary for downloading the CSV data file.
- **csv**: Enables efficient reading and parsing of CSV files for transformation and loading.

Add these dependencies to your `Cargo.toml` file:

```toml
[dependencies]
rusqlite = "0.26"
structopt = "0.3.25"
reqwest = { version = "0.11", features = ["blocking"] }
csv = "1.1"
```

To install the dependencies, run:

```bash
cargo build
```

## Project Overview
This project includes both an ETL process and CRUD functionality, both implemented in Rust. Here’s a high-level overview:

### ETL Process
The ETL process downloads a CSV file of chess player transfers, transforms the data, and loads it into an SQLite database.

### CRUD Operations
The CLI allows CRUD commands for database interactions.

- **Extract**: Download the CSV file from a public URL.
- **Transform**: Parse and process relevant fields from the CSV.
- **Create**: Add a new transfer record.
- **ReadLatest**: Retrieve the most recent transfer record.
- **Update**: Modify an existing record.
- **Delete**: Remove a record by ID.

These operations make the program versatile for handling both initial data loading and subsequent modifications.

## How to Run the Program

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Build the Program**:

    ```bash
    cargo build --release
    ```

3. **Run the ETL Process**:
   Run the program with to download, transform, and load data into the SQLite database.

    ```bash
    cargo run -- extract
	cargo run -- load
    ```

4. **Use CRUD Commands**: Interact with the database using the following commands:

    - **Create**: Add a new record

      ```bash
      cargo run create --url "example.com" --player-id 123 --federation "USA" --former-fed "THA" --transfer-date "2004-02-01"
      ```

    - **ReadLatest**: Fetch the most recent record

      ```bash
      cargo run read-latest
      ```

    - **Update**: Modify an existing record by ID

      ```bash
      cargo run update --id 1 --new-url "newurl.com"
      ```

    - **Delete**: Remove a record by ID

      ```bash
      cargo run delete --id 1
      ```

## GitHub Copilot Usage
GitHub Copilot was used to assist in writing boilerplate code, particularly for repetitive patterns and Rust’s error handling. It helped quickly generate function signatures, SQL query structures, and set up command-line argument parsing, speeding up development.

## LLM Usage
An AI language model (LLM) was used extensively to refine complex logic, troubleshoot issues, and provide Rust-specific best practices, such as error handling and lifetime management. The LLM guidance enhanced the program's reliability and modularity by suggesting a clear structure for the ETL and CRUD modules.

## Artifact
artifact can be downloaded here