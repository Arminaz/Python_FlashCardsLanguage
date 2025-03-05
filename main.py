# Imports
from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# UI
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer_loop=None
current_word=None

# File Access
data = pandas.read_csv("data/words_to_learn.csv")
to_learn = data.to_dict(orient="records")
photo_front = PhotoImage(file="images/card_front.png")
photo_back = PhotoImage(file="images/card_back.png")

# Wrong Guess
def wrong_guess():
    generate_word()


# Correct Guess
def correct_guess():
    global current_word
    word_index = data[((data["Arabic"] == current_word["Arabic"]) & (data["English"] == current_word["English"]))].index
    data.drop(word_index)
    generate_word()

# Generate Word
def generate_word():
    global current_word
    current_word = random.choice(to_learn)
    canvas_front.itemconfig(canvas_image, image=photo_front)
    canvas_front.itemconfig(language_text, text="Arabic")
    canvas_front.itemconfig(word_text, text=f"{current_word["Arabic"]}")
    guess_word()


# Guess Word
def guess_word():
    global timer_loop
    timer_loop=window.after(3000, flip_card)

# Flip Card
def flip_card():
    global current_word
    global timer_loop
    window.after_cancel(timer_loop)
    canvas_front.itemconfig(canvas_image, image=photo_back)
    canvas_front.itemconfig(language_text, text="English")
    canvas_front.itemconfig(word_text, text=f"{current_word["English"]}")

# Canvas Front
canvas_front = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas_front.create_image(405, 275, image=photo_front)
canvas_front.grid(column=1, row=1, columnspan=2)

# Words
language_text = canvas_front.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas_front.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))


# Wrong Image
wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0, command=wrong_guess)
button_wrong.grid(column=1, row=2)

# Write Image
right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0, command=correct_guess)
button_right.grid(column=2, row=2)


generate_word()


window.mainloop()






