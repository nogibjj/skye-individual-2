"""Query the database"""

import logging
from databricks import sql
from .utils import get_env_variables

DB_name = "transfer"
DB = DB_name + ".db"

query = """
    WITH latest_transfer_per_federation AS (
        SELECT 
            federation, 
            MAX(transfer_date) AS latest_transfer_date
        FROM transfer
        GROUP BY federation)
    
    SELECT 
        l.federation,
        COUNT(t.id) AS transfer_count,
        l.latest_transfer_date
    FROM latest_transfer_per_federation l
    JOIN transfer t
    ON l.federation = t.federation
    GROUP BY l.federation, l.latest_transfer_date
    ORDER BY l.latest_transfer_date DESC;   
    """


def query():
    logger = logging.getLogger("urbanGUI")
    hostname, access_token, http_path = get_env_variables()
    with sql.connect(
        server_hostname=hostname,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        logger.info("Query executed successfully. Printing result...")
        logger.debug(result)
