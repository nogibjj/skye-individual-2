from dotenv import load_dotenv
import logging
import os

HOST_KEY = "HOST"
ACCESS_TOKEN_KEY = "ACCESS_TOKEN"
PATH_KEY = "HTTP_PATH"


def get_env_variables():
    load_dotenv()
    hostname = os.getenv(HOST_KEY)
    if not hostname:
        raise ValueError("HOST is not set")

    access_token = os.getenv(ACCESS_TOKEN_KEY)
    if not access_token:
        raise ValueError("ACCESS_TOKEN is not set")

    http_path = os.getenv(PATH_KEY)
    if not http_path:
        raise ValueError("PATH is not set")
    return hostname, access_token, http_path


def handle_error(e):
    logger = logging.getLogger("urbanGUI")
    logger.error(f"Error : {e}")
    raise e
