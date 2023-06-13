from course import get_course, today
from tkinter import *

window = Tk()
window.title("Банк")
window.geometry("500x500")
window.resizable(width=False, height=False)

img_logo = PhotoImage(file=r"D:\Kod\modul 2\lesson8\logo.png")
logo = Label(window, image=img_logo)
logo.place(x=0, y=0)

title_label = Label(window, text="Банк Maxmum", font="TimesNewsRoman 34")
title_label.place(x=160, y=50)

course_label = Label(window, text=f"Курсы валют на {today} число:", font="TimesNewsRoman 20")
course_label.place(x=35, y=160)

dollar_info =f"{get_course('R01235').get('name')} {get_course('R01235').get('value')} руб."
dollar_label = Label(window, text=dollar_info, font="TimesNewsRoman 16")
dollar_label.place(x=80, y=215)

eur_info =f"{get_course('R01239').get('name')} {get_course('R01239').get('value')} руб."
eur_label = Label(window, text=eur_info, font="TimesNewsRoman 16")
eur_label.place(x=80, y=245)

cny_info =f"{get_course('R01375').get('name')} {get_course('R01239').get('value')} руб."
cny_label = Label(window, text=cny_info, font="TimesNewsRoman 16")
cny_label.place(x=80, y=275)

entry = Entry(font="TimesNewsRoman 16", width=10)
entry.place(x=80, y=400)

y = 30


def search():
    global y

    currency_id = entry.get()
    currency_info = f"{get_course(currency_id).get('name')} {get_course(currency_id).get('value')} руб."
    currency_lable = Label(window, text=currency_info, font="TimesNewsRoman 16")
    currency_lable.place(x=80, y=245 + y)

button = Button(text="Поиск", font="TimesNewsRoman 10", command=search)
button.place(x=200, y=400)


window.mainloop()
