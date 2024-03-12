import requests
from bs4 import BeautifulSoup
import csv


def parse_cmicki(url, writer):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cmicki = soup.find_all(class_="showcase-item-3")
    
    for cmicka in cmicki:
        # print(cmicka)
        name = cmicka.find(class_="showcase-name-first").text
        description = cmicka.find(class_="showcase-name-second").text
        code = cmicka.find(class_="product-code").text
        price = cmicka.find(itemprop="price")['content']
        writer.writerow([name, description, code, price])


if __name__ == "__main__":
    base_url = 'https://mirm.ru/catalog/orkectrovie-inctrumenti/cmichkovie-inctrumenti/'
    all_cmicki_data = []
    with open('cmicki.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Описание', 'Артикул', 'Цена'])  
            for page in range(1,6):
                url = f'{base_url}?PAGEN_1={page}'
                parse_cmicki(url, writer)



