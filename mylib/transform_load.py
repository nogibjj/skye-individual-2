import sqlite3
import csv
import os

DB_name = "transfer"
DB = DB_name + ".db"


def load(dataset="data/transfer.csv"):
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {DB_name}")
    cursor.execute(
        f"""CREATE TABLE {DB_name} 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL, 
    player_id INTEGER NOT NULL, 
    federation CHARACTER NOT NULL,
    former_fed CHARACTER NOT NULL, 
    transfer_date TEXT NOT NULL)"""
    )

    cursor.executemany(
        f"""INSERT INTO {DB_name} (url,
    player_id,
    federation,
    former_fed,
    transfer_date
    )
    VALUES (?,?, ?, ?, ?)
    """,
        payload,
    )
    conn.commit()
    conn.close()
    return "transfer.db"
