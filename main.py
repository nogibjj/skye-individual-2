"""
ETL-Query script
"""
import logging
import argparse
import sys

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main():
    # Execute the chosen step
    extract()
    load()
    query()


if __name__ == "__main__":
    main()