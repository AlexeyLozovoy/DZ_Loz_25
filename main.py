# Найти на фриланс-биржах (например https://freelancehunt.com) заказ на парсинг HTML страниц (можно не активный) и сделать по нему задание. Если заказ большой, можно сделать только несколько пунктов на выбор
# Форма сдачи - скрипты парсинга и ссылка на задание

# https://freelancehunt.com/project/parsing-gugl-tablitsyu/1175665.html

import requests, sys, openpyxl, time
from bs4 import BeautifulSoup

while True:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    response = requests.get('https://kurs.com.ua/valyuta/eur', headers=headers)
    content = response.content

    if response.status_code == 200:
        response = response.text
    else:
        sys.exit()

    soup = BeautifulSoup(content, 'html.parser')
    euro_rate = soup.find('td', class_='td-green').find('div', class_='course').text[0:7]

    print("Курс евро на сайте Kurs.com.ua:", euro_rate)

    wb = openpyxl.load_workbook('kurs.xlsx')
    ws = wb.active
    ws['A1'] = 'Курс евро на сайте Kurs.com.ua:'
    ws['B1'] = euro_rate
    wb.save('kurs.xlsx')

    time.sleep(10)
