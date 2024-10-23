from setuptools import setup, find_packages

setup(
    name="chess_transfer",
    version="1.0.0",
    description="The package provides functionality to retrieve the latest transfer dates and counts for each federation",
    author="Skye A.",
    author_email="skye.augsorn@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
)