import requests
from bs4 import BeautifulSoup

currency_date = input("Введите дату в формате 01/01/2020 ")

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params={"date_req": currency_date})
soup = BeautifulSoup(response.content, features="xml")


def check_currency(currency_id):
    australian_currency = soup.find("Valute", ID=currency_id)

    currency_nominal = australian_currency.Nominal.text
    currency_name = australian_currency.Name.text
    currency_value = australian_currency.Value.text

    print(f'({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} рублей.')

# check_currency("R01010")
# check_currency("R01020A")
# check_currency("R01035")


currencies_list = soup.find_all("Valute")
for currency in currencies_list:
    check_currency(currency["ID"])
