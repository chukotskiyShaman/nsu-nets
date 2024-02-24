import requests
from bs4 import BeautifulSoup
import csv


def parse_website(url):
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        #код для извлечения нужных данных
        logo = [soup.find('img')['src'],
                soup.find('meta', attrs={"name": "keywords"})['content'],
                soup.find('meta', attrs={"name": "geo.placename"})['content'],
                soup.find('a', attrs={"class": "logo2023"})['href']]
        return logo
    else:
        print("Ошибка при получении данных", response.status_code)
        return None


def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Some Logo", data[0]])
        writer.writerow(["Name", data[1]])
        writer.writerow(["Address", data[2]])
        writer.writerow(["Logo2023 :D", data[3]])

url = 'http://www.sch112.edusite.ru/'
parsed_data = parse_website(url)

if parsed_data:
    save_to_csv(parsed_data, 'parsed_data.csv')
    print("Данные сохранены в файл")
else:
    print("Ошибка при зарписи данных")
