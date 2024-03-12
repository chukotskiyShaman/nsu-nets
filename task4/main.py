import csv

from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from bs4 import BeautifulSoup


url = 'https://mirm.ru/catalog/orkectrovie-inctrumenti/cmichkovie-inctrumenti/'

def make_soup(url):
    # print("Я великий суп")
    # print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def parse_cmicki(url):
    # print("Я в миске")
    # print(url)
    soup = make_soup(url)
    cmicki = soup.find_all(class_="showcase-item-3")

    all_data = []
    for cmicka in cmicki:
        print(cmicka)
        name = cmicka.find(class_="showcase-name-first").text
        description = cmicka.find(class_='showcase-name-second').text
        code = cmicka.find(class_="product-code").text
        price = cmicka.find(itemprop="price")['content']
        data_rows = [name, description, code, price]
        all_data.append(data_rows)
    return all_data



app = FastAPI()

@app.get('/')
async def parse_url():
    print("Я в парсе урл")
    request = requests.get('https://mirm.ru/catalog/orkectrovie-inctrumenti/cmichkovie-inctrumenti/')
    parsed_data = parse_cmicki(url)
    return JSONResponse(content=parsed_data)


