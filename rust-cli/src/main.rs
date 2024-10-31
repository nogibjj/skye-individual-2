mod cli;
mod extract;
mod query;
mod transform_load;

use cli::cli;
use rusqlite::{Result};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Call the ETL process function
    cli()
}
