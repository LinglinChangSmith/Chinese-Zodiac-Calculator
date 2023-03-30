from tkinter import *
BG_COLOR = "#282A3A"
TEXT_COLOR = "#fbb762"

window = Tk()
window.title("Chinese Zodiac Calculator")
window.config(padx=50, pady=50, bg=BG_COLOR)


def get_zodiac():
    year = user_input.get()
    if not year.isnumeric():
        canvas.itemconfig(beginning_canvas, image=error_img)
    elif int(year) >= 10000:
        canvas.itemconfig(beginning_canvas, image=warning_img)
    elif year[0] == "0":
        canvas.itemconfig(beginning_canvas, image=error_img)
    else:
        year_modulo = int(year) % 12
        if year_modulo == 0:
            canvas.itemconfig(beginning_canvas, image=monkey_img)
        elif year_modulo == 1:
            canvas.itemconfig(beginning_canvas, image=rooster_img)
        elif year_modulo == 2:
            canvas.itemconfig(beginning_canvas, image=dog_img)
        elif year_modulo == 3:
            canvas.itemconfig(beginning_canvas, image=pig_img)
        elif year_modulo == 4:
            canvas.itemconfig(beginning_canvas, image=rat_img)
        elif year_modulo == 5:
            canvas.itemconfig(beginning_canvas, image=ox_img)
        elif year_modulo == 6:
            canvas.itemconfig(beginning_canvas, image=tiger_img)
        elif year_modulo == 7:
            canvas.itemconfig(beginning_canvas, image=rabbit_img)
        elif year_modulo == 8:
            canvas.itemconfig(beginning_canvas, image=dragon_img)
        elif year_modulo == 9:
            canvas.itemconfig(beginning_canvas, image=snake_img)
        elif year_modulo == 10:
            canvas.itemconfig(beginning_canvas, image=horse_img)
        elif year_modulo == 11:
            canvas.itemconfig(beginning_canvas, image=goat_img)


def clear_placeholder(event):
    user_input.delete(0, END)


window.bind("<Return>", lambda event: get_zodiac())

title = Label(text="FIND OUT YOUR SIGN", font=("Courier", 40, "bold"))
title.config(bg=BG_COLOR, fg=TEXT_COLOR)
title.grid(row=0, column=0, columnspan=2)

user_input = Entry(width=40)
user_input.insert(0, "Enter your birth year here")
user_input.grid(row=1, column=0, pady=20)
user_input.bind("<Button-1>", clear_placeholder)

calculate_btn = Button(text="Calculate", background=BG_COLOR, highlightthickness=0, borderwidth=0, command=get_zodiac)
calculate_btn.grid(row=1, column=1, pady=20)

canvas = Canvas(width=600, height=600, bg=BG_COLOR, highlightthickness=0)
beginning_img = PhotoImage(file="images/Default.png")
error_img = PhotoImage(file="images/Error.png")
warning_img = PhotoImage(file="images/Warning.png")
monkey_img = PhotoImage(file="images/Monkey.png")
dog_img = PhotoImage(file="images/Dog.png")
dragon_img = PhotoImage(file="images/Dragon.png")
goat_img = PhotoImage(file="images/Goat.png")
horse_img = PhotoImage(file="images/Horse.png")
ox_img = PhotoImage(file="images/Ox.png")
pig_img = PhotoImage(file="images/Pig.png")
rabbit_img = PhotoImage(file="images/Rabbit.png")
rat_img = PhotoImage(file="images/Rat.png")
rooster_img = PhotoImage(file="images/Rooster.png")
snake_img = PhotoImage(file="images/Snake.png")
tiger_img = PhotoImage(file="images/Tiger.png")
beginning_canvas = canvas.create_image(300, 300, image=beginning_img)
canvas.grid(row=2, column=0, columnspan=2)

window.mainloop()

