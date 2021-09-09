from tkinter import *
from data_manager import DataManager, Pair

BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#000000"
WHITE = "#FFFFFF"
timer_function = None
pair: Pair


def known_button():
    data_manager.remove_pair(pair)
    data_manager.save_pairs()
    change_card()


def change_card():
    global timer_function, pair

    if timer_function is not None:
        window.after_cancel(timer_function)

    pair = data_manager.get_pair()
    canvas.itemconfig(card_bg, image=front)
    canvas.itemconfig(card_title, text=Pair.get_question_title(), fill="black")
    canvas.itemconfig(card_content, text=pair.question, fill="black")
    timer_function = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_bg, image=back)
    canvas.itemconfig(card_title, text=Pair.get_answer_title(), fill="white")
    canvas.itemconfig(card_content, text=pair.answer, fill="white")
    window.after_cancel(timer_function)


data_manager = DataManager()
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_content = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

img_correct = PhotoImage(file="./images/right.png")
bt_correct = Button(image=img_correct, highlightthickness=0, command=known_button)
img_wrong = PhotoImage(file="./images/wrong.png")
bt_wrong = Button(image=img_wrong, highlightthickness=0, command=change_card)
bt_correct.grid(column=0, row=1)
bt_wrong.grid(column=1, row=1)

change_card()
window.mainloop()
