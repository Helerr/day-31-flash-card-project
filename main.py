import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

screen = Tk()
screen.title("Flash Card Game")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
wrong_button_image = PhotoImage(file="./images/wrong.png")
right_button_image = PhotoImage(file="./images/right.png")

flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.create_image(400, 263, image=card_front_image)
flash_card.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
flash_card.create_text(400, 263, text="Word", font=WORD_FONT)
flash_card.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_button_image, highlightthickness=0, bd=0)
right_button.grid(row=1, column=1)

screen.mainloop()
