use rusqlite::{Connection, Result};
use std::error::Error;
use structopt::StructOpt;

use crate::query::{create_transfer, delete_transfer, read_latest_transfer, update_transfer};

/// CLI program for managing transfer records
#[derive(StructOpt)]
struct Cli {
    #[structopt(subcommand)]
    command: Command,
}

#[derive(StructOpt)]
enum Command {
    /// Create a new transfer record
    Create {
        url: String,
        player_id: i32,
        federation: String,
        former_fed: String,
        transfer_date: String,
    },
    /// Read the latest transfer record
    ReadLatest,
    /// Update the URL of an existing transfer record by ID
    Update { id: i32, new_url: String },
    /// Delete a transfer record by ID
    Delete { id: i32 },
}

const DB_NAME: &str = "transfer.db";

pub fn cli() -> Result<(), Box<dyn Error>> {
    let args = Cli::from_args();

    // Open a connection to the SQLite database
    let connection = Connection::open(DB_NAME)?;

    // Execute the command based on user input
    match args.command {
        Command::Create {
            url,
            player_id,
            federation,
            former_fed,
            transfer_date,
        } => create_transfer(
            &connection,
            &url,
            player_id,
            &federation,
            &former_fed,
            &transfer_date,
        )?,

        Command::ReadLatest => {
            if let Some(id) = read_latest_transfer(&connection)? {
                println!("Latest record ID: {}", id);
            } else {
                println!("No records found.");
            }
        }

        Command::Update { id, new_url } => update_transfer(&connection, id, &new_url)?,

        Command::Delete { id } => delete_transfer(&connection, id)?,
    }

    Ok(())
}
