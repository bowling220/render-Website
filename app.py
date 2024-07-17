import requests
from bs4 import BeautifulSoup
import json

url = 'https://scores.bowl.com/2024-JG/Qualifying_Round%201_U18Boys.pdf?v=new'  # Replace with your target URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find_all('p')
results = [item.get_text() for item in data]

with open('data.json', 'w') as f:
    json.dump(results, f)
