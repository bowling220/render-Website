from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    url = 'https://scores.bowl.com/2024-JG/Qualifying_Round%201_U18Boys.pdf?v=new'  # Replace with your target URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find_all('p')
    results = [item.get_text() for item in data]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
