from tkinter import *
import random

window = Tk()
window.geometry("600x600")

window.title("Алхимик")


class Clay:
    image = PhotoImage(file=r'D:\Kod\modul 2\modul3\lesson7\images\pottery.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Ceramics


class Ceramics:
    image = PhotoImage(file=r'D:\Kod\modul 2\modul3\lesson7\images\ceramics.png').subsample(4, 4)


class Water:
    image = PhotoImage(file=r'D:\Kod\modul 2\modul3\lesson7\images\water.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Ground):
            return Clay
        elif isinstance(other, Fire):
            return Steam


class Steam:
    image = PhotoImage(file=r'D:\Kod\modul 2\modul3\lesson7\images\aroma.png').subsample(4, 4)


class Fire:
    image = PhotoImage(file=r'D:\Kod\modul 2\modul3\lesson7\images\fire.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam
        elif isinstance(other, Clay):
            return Ceramics


class Ground:
    image = PhotoImage(file=r'D:\Kod\modul 2\modul3\lesson7\images\ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Clay


class Wind:
    image = PhotoImage(file=r'D:\Kod\modul 2\modul3\lesson7\images\wind.png').subsample(4, 4)


canvas = Canvas(width=600, height=600)
canvas.pack()

elements = [Water(), Fire(), Ground(), Wind()]

for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)


def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        elem_id_1, elem_id_2 = images_ids[0], images_ids[1]

        elem_1 = elements[elem_id_1 - 1]
        elem_2 = elements[elem_id_2 - 1]
        new_elem = elem_1 + elem_2

        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)

    canvas.coords(images_ids, event.x, event.y)


window.bind("<B1-Motion>", move)

window.mainloop()
