from gtts import gTTS

my_file = open('test.txt', "r", encoding="utf-8")
my_str = my_file.read()
my_file.close()

render = gTTS(text=my_str, lang="ru")
render.save("i love python.mp3")

