"""Query the database"""

import sqlite3
import logging

DB_name = "transfer"
DB = DB_name + ".db"
logger = logging.getLogger("urbanGUI")


def get(id):
    """Query the database"""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {DB_name} WHERE id = ?", [str(id)])
    logging.info(f"row {id} of the {DB}")
    logging.debug(cursor.fetchall())
    conn.close()


def get_all():
    """Query the database"""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {DB_name}")
    logging.info(f"All rows of the {DB_name} table:")
    logging.debug(cursor.fetchall())
    conn.close()


def get_all_with_limit(limit=10):
    """Query the database with default limit = 10"""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {DB_name} LIMIT {limit}")
    logging.info(f"{limit} rows of the {DB_name} table:")
    logging.debug(cursor.fetchall())
    conn.close()


def create(url, player_id, federation, former_fed, transfer_date):
    """Create a new entry"""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO {DB_name} 
        (url, player_id, federation, former_fed, transfer_date) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (url, player_id, federation, former_fed, transfer_date),
    )
    conn.commit()
    logging.info(
        f"create new entry"
        f"value: {url},{player_id}, {federation}"
        f"{former_fed}, {transfer_date}"
    )
    conn.close()
    return cursor.lastrowid


def update(
    id,
    url="url",
    player_id=12345,
    federation="federation",
    former_fed="former_fed",
    transfer_date="01-01-2004",
):
    """Update"""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        f"""
        UPDATE {DB_name} 
        SET url=?, 
            player_id=?, 
            federation=?, 
            former_fed=?, 
            transfer_date=? 
        WHERE id=?
        """,
        (url, player_id, federation, former_fed, transfer_date, id),
    )
    conn.commit()
    logging.info(
        f"update row {id}"
        f"updated value :{url}, {player_id}, "
        f"{federation}, {former_fed}, {transfer_date}"
    )
    conn.close()


def delete(id):
    """Delete a record"""
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {DB_name} WHERE id=?", [str(id)])
    conn.commit()
    logging.info(f"data no.{id} is deleted")
    conn.close()
