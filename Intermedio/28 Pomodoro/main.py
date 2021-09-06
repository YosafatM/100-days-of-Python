from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

is_counting = False
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps, is_counting

    if timer is not None:
        window.after_cancel(timer)
        lb_title.config(text="Timer", fg=GREEN)
        canvas.itemconfig(count_text, text="00:00")
        lb_checks["text"] = ""
        timer = None
        reps = 0
        is_counting = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global is_counting, reps

    if is_counting:
        pass

    reps += 1
    if reps % 8 == 0:
        lb_title.config(text="Break", fg=RED)
        minutes = LONG_BREAK_MIN
    elif reps % 2 == 0:
        lb_title.config(text="Break", fg=PINK)
        minutes = SHORT_BREAK_MIN
    else:
        lb_title.config(text="Work", fg=GREEN)
        minutes = WORK_MIN

    is_counting = True
    count_down(minutes * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    minutes = count // 60
    seconds = count % 60
    seconds = f"0{seconds}" if seconds < 10 else seconds

    canvas.itemconfig(count_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif reps % 2 == 1:
        global is_counting
        is_counting = False
        lb_checks["text"] += "✅"
        start_timer()  # Break


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

bt_start = Button(text="Start", highlightthickness=0, command=start_timer)
bt_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

lb_checks = Label(text="", fg=GREEN, bg=YELLOW)
lb_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))

lb_title.grid(column=1, row=0)
canvas.grid(column=1, row=1)
bt_start.grid(column=0, row=2)
bt_reset.grid(column=2, row=2)
lb_checks.grid(column=1, row=3)

window.mainloop()
