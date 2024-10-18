import pandas as pd
import logging
from databricks import sql
from .utils import get_env_variables, handle_error


DB_name = "transfer"
DB = DB_name + ".db"
dataset = "data/transfer.csv"


def load(dataset=dataset):
    logger = logging.getLogger("urbanGUI")

    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    hostname, access_token, http_path = get_env_variables()

    try:
        with sql.connect(
            server_hostname=hostname,
            http_path=http_path,
            access_token=access_token,
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {DB_name}")
            cursor.execute(
                f"""CREATE TABLE {DB_name} 
            (id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            url STRING NOT NULL, 
            player_id INT NOT NULL, 
            federation STRING NOT NULL,
            former_fed STRING NOT NULL, 
            transfer_date STRING NOT NULL)"""
            )
            logger.info("creating table : success")

            cursor.executemany(
                f"""INSERT INTO {DB_name} (url,
            player_id,
            federation,
            former_fed,
            transfer_date
            )
            VALUES (?,?,?,?,?)""",
                [tuple(row) for row in df.itertuples(index=False, name=None)],
            )
            logger.info("inserting data into table : success")
            cursor.close()
    except Exception as e:
        handle_error(e)
    finally:
        if connection:
            connection.close()
            logger.info("Connection closed.")
