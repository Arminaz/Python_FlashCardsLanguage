# Imports
from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# UI
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Front
canvas_front = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_front = PhotoImage(file="images/card_front.png")
canvas_front.create_image(405, 275, image=photo_front)
canvas_front.grid(column=1, row=1, columnspan=2)

# Words
language_text = canvas_front.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas_front.create_text(400, 263, text="World", fill="black", font=("Ariel", 60, "bold"))


# Wrong Image
wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightthickness=0)
button_wrong.grid(column=1, row=2)

# Write Image
right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image, highlightthickness=0)
button_right.grid(column=2, row=2)




window.mainloop()






