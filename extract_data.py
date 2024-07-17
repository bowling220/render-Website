import PyPDF2
import json
import requests
from io import BytesIO

def extract_data_from_pdf(pdf_url):
    response = requests.get(pdf_url)
    pdf_file = BytesIO(response.content)
    reader = PyPDF2.PdfFileReader(pdf_file)
    data = []
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        text = page.extract_text()
        data.append(text)
    return data

pdf_url = "https://scores.bowl.com/2024-JG/Qualifying_Round%201_U18Boys.pdf?v=new"
data = extract_data_from_pdf(pdf_url)

with open("data.json", "w") as f:
    json.dump(data, f)
