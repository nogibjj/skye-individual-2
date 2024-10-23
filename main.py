"""
ETL-Query script
"""
import logging
import argparse
import sys

from mylib.log import init_log
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main():
    init_log()
    logger = logging.getLogger('urbanGUI')

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Data Pipeline CLI")
    parser.add_argument('step', choices=['extract', 'transform', 'load', 'query'],
                        help="Choose the step to execute")

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit("Error: No step specified. Please choose a step to execute.")

    args = parser.parse_args()

    # Execute the chosen step
    if args.step == 'extract':
        logger.debug("Extracting data...")
        logging.info(extract())

    elif args.step == 'load':
        logger.debug("Loading data...")
        logging.info(load())

    elif args.step == 'query':
        logger.debug("Querying data...")
        logging.info(query())


if __name__ == "__main__":
    main()