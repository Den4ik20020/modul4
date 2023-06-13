import vk_api
import random
from cb_RF import get_dollar_course
from swap import check_starships, starships_api
from swap_speed import check_starships_speed

token = "vk1.a.T3Xrm3KnKq7NNsLZFdcMwxadnkGCu-UYlEwreuQZnPUfBqPPIOd37kfZkB9Q1XW6eQomMj6nRuJfSCJ8R8eM8aYVAqXnQmKJu1fJEWOSZfs10exusIGvVEyvdv_cozOhXP1VTE-6VtXivMPRT1ecE7ceOkzMCegB3-UtATZrM5iVofd23x5O2cn0n2DVCPOzQk6ZU0yM6jUcVaUVfkQL4g"

vk = vk_api.VkApi(token=token)
check_starships(starships_api)
while True:
    messages = vk.method("messages.getConversations", {"filter": "unanswered"})
    if messages['count'] > 0:
        user_message = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']

        if user_message.lower() == "курс":
            ans = f'Курс доллара на сегодня {get_dollar_course()} руб.'

        elif user_message.lower() == "планеты":
            ans = f'{check_starships(starships_api)}'
        elif user_message.lower() == "корабли":
            ans = f'{check_starships_speed(starships_api)}'
        else:
            ans = 'Неизвестная команда'

        vk.method("messages.send", {
            "random_id": random.randint(-10 ** 7, 10**7),
            "message": ans,
            "user_id": user_id,
        })
