import yaml
import requests
from bs4 import BeautifulSoup
from pathlib import Path

from data.page_data.parser import parser

def get_credentials(logger):
    url = "https://demo.guru99.com/index.php"
    valid_email = parser("home_page.yml")["valid_email_exaple"]

    data = {
        'emailid': valid_email
    }

    response = requests.post(url, data=data)

    relative_path = "../data/credentials.yml"
    file_path = Path(__file__).parent / relative_path

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        
        uname = soup.find('td', string='User ID :').find_next_sibling('td').string.strip()
        pword = soup.find('td', string='Password :').find_next_sibling('td').string.strip()

        data = {
            'username': uname,
            'password': pword
        }

        with open(file_path, 'w') as file:
            yaml.dump(data, file)

        logger.info(f"Successfully got credentials and saved to '{relative_path}'")

    else:
        logger.info(f"Failed to retrieve data. Status code: {response.status_code}")