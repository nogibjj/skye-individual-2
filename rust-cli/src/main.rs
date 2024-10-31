mod cli;
mod extract;
mod query;
mod transform_load;

use cli::cli;
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

    Ok(())
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Call the ETL process function
    run_etl_process()?;
    cli()
}
