use rusqlite::{params, Connection, Result};
use std::error::Error;

// Insert a new record (Create)
pub fn create_transfer(
    connection: &Connection,
    url: &str,
    player_id: i32,
    federation: &str,
    former_fed: &str,
    transfer_date: &str,
) -> Result<(), Box<dyn Error>> {
    connection.execute(
        "INSERT INTO transfer (url, player_id, federation, former_fed, transfer_date)
         VALUES (?, ?, ?, ?, ?)",
        params![url, player_id, federation, former_fed, transfer_date],
    )?;
    println!("Record inserted successfully");
    Ok(())
}

pub fn read_latest_transfer(connection: &Connection) -> Result<Option<i32>, Box<dyn Error>> {
    let mut stmt = connection.prepare(
        "SELECT id, url, player_id, federation, former_fed, transfer_date
         FROM transfer
         ORDER BY id DESC
         LIMIT 1",
    )?;

    let mut rows = stmt.query([])?;

    if let Some(row) = rows.next()? {
        let id: i32 = row.get(0)?;
        let url: String = row.get(1)?;
        let player_id: i32 = row.get(2)?;
        let federation: String = row.get(3)?;
        let former_fed: String = row.get(4)?;
        let transfer_date: String = row.get(5)?;

        println!(
            "Latest Record - ID: {}, URL: {}, Player ID: {}, Federation: {}, Former Federation: {}, Transfer Date: {}",
            id, url, player_id, federation, former_fed, transfer_date
        );

        Ok(Some(id)) // Return the ID of the latest record
    } else {
        println!("No records found.");
        Ok(None) // Return None if there are no records
    }
}

// Update a specific record (Update)
pub fn update_transfer(
    connection: &Connection,
    id: i32,
    new_url: &str,
) -> Result<(), Box<dyn Error>> {
    connection.execute(
        "UPDATE transfer SET url = ?1 WHERE id = ?2",
        params![new_url, id],
    )?;
    println!("Record updated successfully");
    Ok(())
}

// Delete a specific record (Delete)
pub fn delete_transfer(connection: &Connection, id: i32) -> Result<(), Box<dyn Error>> {
    connection.execute("DELETE FROM transfer WHERE id = ?1", params![id])?;
    println!("Record deleted successfully");
    Ok(())
}
