import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from cb_RF import get_course
from wiki import get_article

token = "vk1.a.T3Xrm3KnKq7NNsLZFdcMwxadnkGCu-UYlEwreuQZnPUfBqPPIOd37kfZkB9Q1XW6eQomMj6nRuJfSCJ8R8eM8aYVAqXnQmKJu1fJEWOSZfs10exusIGvVEyvdv_cozOhXP1VTE-6VtXivMPRT1ecE7ceOkzMCegB3-UtATZrM5iVofd23x5O2cn0n2DVCPOzQk6ZU0yM6jUcVaUVfkQL4g"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        random_id = random.randint(-10 ** 7, 10 ** 7)
        user_id = event.user_id
        if msg[:2] == "-к":
            response = 'Доллар стоит {0} руб.\nЕвро стоит {1} руб.\nЮань стоит {2} руб.'.format(
                get_course('R01235'),
                get_course('R01239'),
                get_course('R01375')
            )
        elif msg[:2] == "-в":
            article = msg[2:]
            response = get_article(article)
        else:
            response = 'Неизвестная команда'
        vk.messages.send(
            user_id=user_id,
            random_id=random_id,
            message=response
        )

# R01235
# R01239
# R01375

