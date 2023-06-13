import requests

response = requests.get("https://swapi.dev/api/")
data = response.json()

planets_url = data["planets"]

# planets_respons = requests.get(planets_url)


def get_planets_info(root_url):

    planets_list = []

    new_planets_list = []

    for i in range(1, 6):
        response = requests.get(f'{root_url}/{i}')
        print(response.json())
        planets_list.append(int(response.json()["diameter"]))
        new_planets_list.append(response.json())

    max_diameter = max(planets_list)

    for planet in new_planets_list:
        if int(planet['diameter']) == max_diameter:
            print(planet['name'])


get_planets_info(planets_url)
