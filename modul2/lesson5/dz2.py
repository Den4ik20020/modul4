import requests
maxs=[]
name=[]
url='https://swapi.dev/api' #Подключаемся к API, 200-нормально
response=requests.get(url)
response=response.json()
starships_api = response.get('starships') #API персонажей из звёздных войн

def check_starships(url):
    for i in range(0,5):
        a=['2','3','5','10','13']
        response=requests.get(url+ '/'+a[i]).json()
        maxs.append(int(response['max_atmosphering_speed']))
        name.append(response['name'])
check_starships(starships_api)
maxsv=max(maxs)
b=maxs.index(maxsv)
print(name[b],'с максимальной скоростью',max(maxs))