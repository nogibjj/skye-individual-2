use csv::ReaderBuilder;
use rusqlite::{Connection, Result};
use std::error::Error;

const DATASET: &str = "../data/transfer.csv";

pub fn load(connection: &Connection) -> Result<(), Box<dyn Error>> {
    // Connect to the database

    // Drop and recreate the `transfer` table
    connection.execute("DROP TABLE IF EXISTS transfer", [])?;
    connection.execute(
        "CREATE TABLE transfer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            player_id INTEGER NOT NULL,
            federation TEXT NOT NULL,
            former_fed TEXT NOT NULL,
            transfer_date TEXT NOT NULL
        )",
        [],
    )?;
    println!("Creating table: success");

    // Initialize CSV reader with specified delimiter and header options
    let mut reader = ReaderBuilder::new().from_path(DATASET)?;

    // Prepare the SQL statement for inserting data
    let mut stmt = connection.prepare(
        "INSERT INTO transfer (url, player_id, federation, former_fed, transfer_date)
         VALUES (?, ?, ?, ?, ?)",
    )?;
    // Iterate over each record in the CSV
    for result in reader.records() {
        match result {
            Ok(record) => {
                stmt.execute([&record[0], &record[1], &record[2], &record[3], &record[4]])?;
            }
            Err(err) => {
                eprintln!("Error reading CSV record: {:?}", err);
            }
        }
    }
    println!("Inserting data into table: success");
    Ok(())
}
