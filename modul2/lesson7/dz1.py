import speech_recognition as sr
import random
hello = ["Привет", "Здравствуй", "Позвольте вас поприветствовать!", "Разрешите вас приветствовать!"]
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