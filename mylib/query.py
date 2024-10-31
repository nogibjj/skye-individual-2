"""Query the database"""

import sqlite3

DB = "../transfer.db"


def connect():
    return sqlite3.connect(DB)


# Create a new record (Create)
def create_transfer(
    connection,
    url: str,
    player_id: int,
    federation: str,
    former_fed: str,
    transfer_date: str,
):
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO transfer (url, player_id, federation, former_fed, transfer_date)
        VALUES (?, ?, ?, ?, ?)
    """,
        (url, player_id, federation, former_fed, transfer_date),
    )
    connection.commit()
    print("Record inserted successfully")


# Read the latest record and return its ID (Read latest)
def read_latest_transfer(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT id, url, player_id, federation, former_fed, transfer_date
        FROM transfer
        ORDER BY id DESC
        LIMIT 1
    """
    )
    row = cursor.fetchone()
    if row:
        id, url, player_id, federation, former_fed, transfer_date = row
        print(
            f"""Latest Record - ID: {id},
        URL: {url}, Player ID: {player_id},
        Federation: {federation},
        Former Federation: {former_fed},
        Transfer Date: {transfer_date}"""
        )
        return id
    else:
        print("No records found.")
        return None


# Update a specific record (Update)
def update_transfer(connection, id: int, new_url: str):
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE transfer
        SET url = ?
        WHERE id = ?
    """,
        (new_url, id),
    )
    connection.commit()
    print("Record updated successfully")


# Delete a specific record (Delete)
def delete_transfer(connection, id: int):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM transfer WHERE id = ?", (id,))
    connection.commit()
    print("Record deleted successfully")


# Execute CRUD operations in sequence
def query():
    connection = connect()

    read_latest_transfer(connection)
    # Create a new record (Create)
    create_transfer(connection, "google.com", 123, "USA", "THA", "2004-02-01")

    # Read the latest record and get its ID (Read latest)
    latest_id = read_latest_transfer(connection)
    if latest_id is not None:
        # Update the latest record (Update)
        update_transfer(connection, latest_id, "example.com")

        # Delete the latest record (Delete)
        delete_transfer(connection, latest_id)

        read_latest_transfer(connection)
    else:
        print("No records found to update or delete.")

    connection.close()
    print("CRUD operations completed successfully")
