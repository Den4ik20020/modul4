from tkinter import *

window = Tk()
window.geometry("800x600")
canvas = Canvas(window, width=800, height=600, bg="white")

canvas.pack()


class House:
    def __init__(self, roof_color, wall_color, count_of_windows):
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.count_of_windows = count_of_windows

    def print_info(self):
        print(f"Цвет крыши: {self.roof_color}, цвет стен: {self.wall_color}, кол-во окон: {self.count_of_windows}")

    def build_house(self):
        canvas.create_rectangle(210, 210, 410, 410, fill=self.wall_color, outline="blue")
        canvas.create_polygon(210, 210, 310, 150, 410, 210, fill=self.roof_color, outline="blue")
        canvas.create_rectangle(250, 250, 305, 290, fill="orange", outline="black")

    def __str__(self):
        return "Дом"


house = House(roof_color="green", wall_color="blue", count_of_windows=1)
house.build_house()
# print(house.count_of_windows)
# print(house.roof_color)
# print(house.wall_color)
# house.print_info()
# print("--" * 30)
# house2 = House(roof_color="orange", wall_color="pink", count_of_windows=2)
# house2.print_info()
print(house)
# print(house2.count_of_windows)
# print(house2.roof_color)
# print(house2.wall_color)


# house_address = "Ул. Пушкина д. Колотушкина"
# roof_color = "white"
# wall_color = "red"
#
# house_address2 = "Ул. Пушкина д. Колотушкина"
# roof_color2 = "white"
# wall_color2 = "red"

window.mainloop()
