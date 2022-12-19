from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_dict = {}
# ------------------------- Functions ------------------------------------- #
try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("data/french_words.csv")
    words_dict = words.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


def pick_word():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    word = current_card["French"]
    print(word)
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_background, image=canvas_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    words_dict.remove(current_card)
    data = pd.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    pick_word()

# ------------------------- UI ------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Button
wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, command=pick_word)
button_wrong.grid(column=0, row=1)
right = PhotoImage(file="./images/right.png")
button_right = Button(image=right, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

# Canvas
canvas = Canvas(width=800, height=526)
canvas_img = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=canvas_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_back = PhotoImage(file="./images/card_back.png")
pick_word()

window.mainloop()
