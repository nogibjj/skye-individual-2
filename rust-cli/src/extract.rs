use reqwest::blocking::get;
use std::fs::{self, File};
use std::io::Write;
use std::path::Path;

pub fn extract(url: &str, file_path: &str) -> Result<String, Box<dyn std::error::Error>> {
    // Create the directory if it doesn't exist
    if let Some(parent_dir) = Path::new(file_path).parent() {
        fs::create_dir_all(parent_dir)?;
    }

    // Download the file
    let response = get(url)?;
    let mut file = File::create(file_path)?;
    file.write_all(&response.bytes()?)?;

    Ok(file_path.to_string())
}
