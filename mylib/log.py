import logging
# import os

file_path = "log/database_log.log"
#
# # Check if the file exists
# if os.path.exists(file_path):
#     os.remove(file_path)
#

def init_log(file_name=file_path, level=logging.NOTSET):
    logging.basicConfig(
        filename=file_name,
        filemode="a",
        format="""%(asctime)s:%(msecs)d %(levelname)s %(message)s""",
        datefmt="%H:%M:%S",
        level=level,
    )
