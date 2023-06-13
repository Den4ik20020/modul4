from tkinter import *

window = Tk()
window.title("Поздравительная открытка")
window.geometry("800x600")
window.resizable(width=False, height=False)
window.config(background="hotpink")


def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l.destroy()


def congratulation():
    clear()
    label = Label(window, text="Пусть весна подарит счастье,\nНастроение и успех.\nПусть обходят вас ненастья,\nИ звучит почаще смех!\nНаслаждайтесь, улыбайтесь.\nОптимизма и добра.\nС праздником 8 Марта!\nВы прекрасны, как всегда!", font="TimesNewsRoman 24", background="hotpink", foreground="blue")
    label.place(x=175, y=50)
    button_home = Button(text="Домой", font="TimesNewsRoman 15", command=homepage)
    button_home.place(x=50, y=550)
    return label, button_home


def homepage():
    clear()
    title_label = Label(window, text="Поздравляю всех девушек\n с наступающим восьмым\n марта!!!",
    font="TimesNewsRoman 34", background="hotpink", foreground="blue")
    title_label.place(x=120, y=50)
    button = Button(text="Поздравление", font="TimesNewsRoman 15", command=congratulation)
    button.place(x=50, y=550)


homepage()

window.mainloop()
