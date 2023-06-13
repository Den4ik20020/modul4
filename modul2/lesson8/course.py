import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime("%d.%m.%Y")
responce = requests.get("http://www.cbr.ru/scripts/XML_daily.asp", params={'date_req':today})

soup = BeautifulSoup(responce.content, features="xml")


def get_course(currency_id):
    data = soup.find("Valute", ID=currency_id)
    currency_name = data.Name.text
    currency_vulue = data.Value.text

    currency_info = {'name' : currency_name, 'value' : currency_vulue}

    return currency_info
