import requests
maxs=[]
name=[]
url='https://swapi.dev/api' #Подключаемся к API, 200-нормально
response=requests.get(url)
response=response.json()
starships_api = response.get('starships') #API персонажей из звёздных войн

def check_starships(url):
    for i in range(0, 8):
        a=['2', '3', '5', '10', '11', '12', '13', '17']
        response=requests.get(url+ '/' + a[i]).json()
        print(response['name'])
        maxs.append(int(response['max_atmosphering_speed'].replace('1000km', '1000')))
        name.append(response['name'])
    maxsv=max(maxs)
    b=maxs.index(maxsv)