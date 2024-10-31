mod extract;
mod query;
mod transform_load;

use query::{create_transfer, delete_transfer, read_latest_transfer, update_transfer};
use rusqlite::{Connection, Result};

const URL: &str = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/chess-transfers/transfers.csv";
const FILE_PATH: &str = "../data/transfer.csv";
const DB_NAME: &str = "../transfer.db";

fn run_etl_process() -> Result<(), Box<dyn std::error::Error>> {
    let connection = Connection::open(DB_NAME)?;

    // Extract data
    extract::extract(URL, FILE_PATH)?;

    // Transform and load data
    transform_load::load(&connection, FILE_PATH)?;

    read_latest_transfer(&connection)?;

    // Query data
    create_transfer(&connection, "google.com", 123, "USA", "THA", "2004-02-01")?;

    // Example of Read
    if let Some(id) = read_latest_transfer(&connection)? {
        println!("Latest record ID: {}", id);

        // Update the latest record (Update)
        update_transfer(&connection, id, "example.com")?;

        // Delete the latest record (Delete)
        delete_transfer(&connection, id)?;

        read_latest_transfer(&connection)?;
    } else {
        println!("No records found to update or delete.");
    }
    println!("ETL process completed successfully.");
    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Call the ETL process function
    run_etl_process()
}
