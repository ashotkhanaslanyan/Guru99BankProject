from pathlib import Path

import yaml

def urls():
    path = Path(__file__).parent / "urls.yml"
    try:
        with open(path) as urls_file:
            data = yaml.load(urls_file, Loader=yaml.FullLoader)
        return data
    finally:
        urls_file.close()