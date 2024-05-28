import os
from pathlib import Path

def clear_credentials(logger):
    relative_path = "../data/credentials.yml"
    file_path = Path(__file__).parent / relative_path

    if os.path.exists(file_path):
        os.remove(file_path)
        logger.info(f"Credentials at '{relative_path}' have been deleted.")