from tkinter import *
import random

window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=600, height=600)
canvas.pack()

backgtound = PhotoImage(file=r"D:\Kod\modul 2\lesson4\photo\bg_2.png")

class Knight:
    def __init__(self):
        self.x = 150
        self.y = 350
        self.v = 0
        self.v_x = 0
        self.photo = PhotoImage(file=r"D:\Kod\modul 2\lesson4\photo\knight.png")

    def up(self, event):
        self.v = -3

    def down(self, event):
        self.v = 3

    def stop(self, event):
        self.v = 0

    def right(self, event):
        self.v_x = 3

    def left(self, event):
        self.v_x = -3


knight = Knight()

class Dragon:
    def __init__(self):
        self.x = random.randint(450, 550)
        self.y = random.randint(50, 550)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file=r"D:\Kod\modul 2\lesson4\photo\dragon.png")


dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=backgtound)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v
    knight.x += knight.v_x
    if knight.y <= 52:
        knight.y = 53
    if knight.y >= 544:
        knight.y = 543
    if knight.x <= 50:
        knight.x = 51
    if knight.x >= 550:
        knight.x = 551
    print(knight.y)
    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        dragon.x -= dragon.v

        if ((knight.x - dragon.x) ** 2 + (knight.y - dragon.y) ** 2) ** 0.5 <50:
            dragons.remove(dragon)

        if dragon.x < 0:
            return  lose()

    if len(dragons) == 0:
        return win()
    window.after(10, game)

def win():
    canvas.create_text(300, 300, font="Verdana 40", text="Вы победили!!!")

def lose():
    canvas.create_text(300, 300, font="Verdana 40", text="Вы проиграли!!!")


window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)
window.bind('<KeyRelease>', knight.stop)


game()
window.mainloop()
