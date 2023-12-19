import requests
from bs4 import BeautifulSoup

url = 'https://example.com/table-page'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    if table:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all(['td', 'th'])
            row_data = [column.text.strip() for column in columns]
            print(row_data)
    else:
        print("No table found on the webpage.")
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
