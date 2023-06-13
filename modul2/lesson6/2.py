import requests
from bs4 import BeautifulSoup

currency_date = input("Введите дату в формате 01/01/2020 ")
currencies_to_show = input("Введите название валюты или начало названия: ").capitalize()

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params={"date_req": currency_date})
soup = BeautifulSoup(response.content, features="xml")

currencies_list = soup.find_all("Valute")

for currency in currencies_list:
    currency_name = currency.Name.text
    currency_nominal = currency.Nominal.text
    currency_value = currency.Value.text

    if currency_name.startswith(currencies_to_show):
        print(f'{currency_name.upper()}\n\tНоминал - {currency_nominal}\n\tКурс - {currency_value}')
        print()
