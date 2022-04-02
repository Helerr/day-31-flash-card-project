import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = {}
words_dictionary = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dictionary)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=card_flash)


def card_flash():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{current_card['English']}", fill="white")


def is_known():
    global current_card, words_dictionary
    words_dictionary.remove(current_card)
    words_to_learn = pandas.DataFrame(words_dictionary)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    words_dictionary = data.to_dict(orient="records")
else:
    words_dictionary = data.to_dict(orient="records")

window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=card_flash)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
wrong_button_image = PhotoImage(file="./images/wrong.png")
right_button_image = PhotoImage(file="./images/right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT, fill="black")
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_button_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
