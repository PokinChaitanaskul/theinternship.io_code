import requests
from bs4 import BeautifulSoup
import json
from flask import Flask

app = Flask(__name__)


def companies_logo():    
    data = {}

    html_context = requests.get("https://theinternship.io/")
    soup = BeautifulSoup(html_context.content, "html.parser")
    logos = soup.find_all("img", {"class":"center-logos"})
    descriptions = soup.find_all("span", {"class":"list-company"})

    for index in range(len(logos)):
        key = logos[index]["src"]
        data[key] = len(descriptions[index].text)


    sorted_data = sorted(data.items(), key = lambda x:x[1])

    # 4.2
    companies_logo = []
    for items in sorted_data:
        value = "htttps://theinternship.io" + items[0]
        company_logo = dict(logo=value)
        companies_logo.append(company_logo)

    companies = dict(companies = companies_logo)
    formatted_companies = json.dumps(companies, indent = 1)

    return formatted_companies


@app.route('/companies/', methods=['GET'])
def get_companies_logo():
    return companies_logo()
