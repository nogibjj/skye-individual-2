"""
ETL-Query script
"""
import logging
from mylib.log import init_log
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import get, get_all, create, update, delete


init_log()
logger = logging.getLogger('urbanGUI')

# Extract
logging.debug("Extracting data...")
logging.info(extract())

# Transform and load
logging.debug("Transforming data...")
logging.info(load())

# Get All
logging.info("Getting all data...")
get_all()

logging.info("Creating a new entry with value google.com, 12345, usa, can, 06/12/2020")
id = create("google.com", 12345, "usa", "can", "06/12/2020")

logging.info("Get last entry")
get(id)

logging.info("Updating entry")
update(id, "facebook.com", 12345, "usa", "can", "06/12/2020")
get(id)

logging.info("Deleting entry")
delete(id)

logging.info("Getting all data...")
get_all()
logging.info(f"notice that id {id} is no longer in the database")
