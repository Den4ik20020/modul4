import requests
maxs = []
name = []
url = 'https://swapi.dev/api' #Подключаемся к API, 200-нормально
response = requests.get(url)
response = response.json()
starships_api = response.get('planets') #API персонажей из звёздных войн

ansv = ''

def check_starships(url):
    for i in range(0, 9):
        a = ['2', '3', '5', '10', '11', '12', '13', '15', '17']
        response = requests.get(url+ '/'+a[i]).json()
        print(response['name'])
        maxs.append(float(response['diameter'].replace(',', '')))
        name.append(response['name'])

    maxsv = max(maxs)
    b = maxs.index(maxsv)
    ansver = f'{name[b]}, с максимальным диаметром , {max(maxs)}'
    return ansver

