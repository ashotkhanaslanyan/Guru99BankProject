import requests
from bs4 import BeautifulSoup

# URL for form submission
url = "https://demo.guru99.com/index.php"

# Email parameter
data = {
    'emailid': 'b@b.com'
}

# Send POST request
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the uid and pass (adjust based on actual HTML structure)
    uid = soup.find('td', string='User ID :').find_next_sibling('td').string.strip()
    pass_ = soup.find('td', string='Password :').find_next_sibling('td').string.strip()
    
    print(f"UID: {uid}")
    print(f"Pass: {pass_}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
