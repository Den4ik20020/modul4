import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь...")
        audio = recognizer.listen(source)

    speech = recognizer.recognize_google(audio, language="ru_RU")
    print(f"Вы сказали: {speech}")

    if speech.lower() == "привет":
        print("И тебе привет")