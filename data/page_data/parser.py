from pathlib import Path

import yaml

def parser(yml_path):
    path = Path(__file__).parent / yml_path
    try:
        with open(path) as urls_file:
            data = yaml.load(urls_file, Loader=yaml.FullLoader)
        return data
    finally:
        urls_file.close()