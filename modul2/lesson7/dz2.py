import speech_recognition as sr
import random
hello = ["Привет", "Здравствуй", "Позвольте вас поприветствовать!", "Разрешите вас приветствовать!"]
films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
recognizer = sr.Recognizer()

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь...")
        audio = recognizer.listen(source)

    speech = recognizer.recognize_google(audio, language="ru_RU")
    print(f"Вы сказали: {speech}")

    if speech.lower() == "привет":
        hi = random.choice(hello)
        print(hi)
    if speech.lower() == "фильм":
        randomfilm = random.choice(films)
        print(randomfilm)

