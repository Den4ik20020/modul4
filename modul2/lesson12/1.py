from tkinter import *
import time

window = Tk()
window.geometry("500x400")
window.resizable(width=False, height=False)
window.title("Аркада")

canvas = Canvas(window, width=500, height=400)
canvas.pack()


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.oval = canvas.create_oval(200, 200, 230, 230, fill=color)
        self.x = 1
        self.y = 1

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        position = self.canvas.coords(self.oval)
        x1, y1, x2, y2 = position

        if x1 < 0:
            self.x = - self.x

        if y1 < 0:
            self.y = - self.y

        if x2 > 500:
            self.x = - self.x

        if y2 > 400:
            self.y = - self.y


class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 230, 320, 245, fill=color)
        self.x = 0

    def drow(self):
        self.canvas.move(self.rect, self.x, 0)
        position = self.canvas.coords(self.rect)
        x1, y1, x2, y2 = position

        if x1 < 0:
            self.x = 0

        if x2 > 500:
            self.x = 0

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

ball = Ball(canvas, color="red")
platform = Platform(canvas, color="green")

window.bind("<Key-Left>", platform.left)
window.bind("<Key-Right>", platform.right)

while True:
    platform.drow()
    ball.draw()
    window.update()
    time.sleep(0.01)
