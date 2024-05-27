import requests
from bs4 import BeautifulSoup

url = "https://demo.guru99.com/index.php"

data = {
    'emailid': 'b@b.com'
}


response = requests.post(url, data=data)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    
    uid = soup.find('td', string='User ID :').find_next_sibling('td').string.strip()
    pass_ = soup.find('td', string='Password :').find_next_sibling('td').string.strip()
    
    print(f"UID: {uid}")
    print(f"Pass: {pass_}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
