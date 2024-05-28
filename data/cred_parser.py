from pathlib import Path

import yaml

def credentials():
    path = Path(__file__).parent / "credentials.yml"
    try:
        with open(path) as cred_file:
            data = yaml.load(cred_file, Loader=yaml.FullLoader)
        return data
    finally:
        cred_file.close()