use reqwest::blocking::get;
use std::fs::{self, File};
use std::io::Write;
use std::path::Path;


const URL: &str = "https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/chess-transfers/transfers.csv";
const FILE_PATH: &str = "../data/transfer.csv";

pub fn extract() -> Result<String, Box<dyn std::error::Error>> {
    // Create the directory if it doesn't exist
    if let Some(parent_dir) = Path::new(FILE_PATH).parent() {
        fs::create_dir_all(parent_dir)?;
    }

    // Download the file
    let response = get(URL)?;
    let mut file = File::create(FILE_PATH)?;
    file.write_all(&response.bytes()?)?;

    Ok(FILE_PATH.to_string())
}
