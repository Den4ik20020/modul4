import requests
maxs=[]
name=[]
url='https://swapi.dev/api' #Подключаемся к API, 200-нормально
response=requests.get(url)
response=response.json()
starships_api = response.get('starships') #API персонажей из звёздных войн

def check_starships_speed(url):
    for i in range(0, 7):
        a=['2', '3', '5', '10', '12', '13', '17']
        response=requests.get(url+ '/' + a[i]).json()
        print(response['name'])
        maxs.append(int(response['max_atmosphering_speed']))
        name.append(response['name'])
    maxsv=max(maxs)
    b=maxs.index(maxsv)
    speed = f'{name[b]}, с максимальной скоростью , {max(maxs)}'
    print(speed)
    return speed

check_starships_speed(starships_api)