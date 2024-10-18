"""
ETL-Query script
"""
import logging
from mylib.log import init_log
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


init_log()
logger = logging.getLogger('urbanGUI')

# Extract
logging.debug("Extracting data...")
logging.info(extract())

# Transform and load
logging.debug("Transforming data...")
logging.info(load())

logging.debug("Query data...")
logging.info(query())
