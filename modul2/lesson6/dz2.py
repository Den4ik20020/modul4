import requests
from bs4 import BeautifulSoup
valute_from = input("Введите код например'EUR': ").upper()
valute_to = input("Введите код например'USD':").upper()
amount = int(input('Кол-во'))
print(valute_from, valute_to)
response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
soup = BeautifulSoup(response.content, features="xml")


def course(valute_from, valute_to, amount):
    currencies_list = soup.find_all("Valute")
    for currency in currencies_list:
        currency = soup.find("Valute", ID=currency["ID"])
        currency_nominal = currency.Value.text
        currency_nominal = currency_nominal.replace(',', '.')
        currency_nominal = float(currency_nominal)
        if valute_to == "RUB":
            code_list = soup.find_all("CharCode")
            for codes in code_list:
                code = codes.text
                if code == valute_from:
                    itog = amount * currency_nominal
        elif valute_from == "RUB":
            code_list = soup.find_all("CharCode")
            for codes in code_list:
                code = codes.text
                if code == valute_to:
                    itog = amount / currency_nominal
        else:
            code_list = soup.find_all("CharCode")
            for codes in code_list:
                code = codes.text
                if code == valute_from:
                    num_one = currency_nominal * amount
                elif code == valute_to:
                    num_two = currency_nominal
            itog = num_one / num_two

    print(itog)


course(valute_from, valute_to, amount)
