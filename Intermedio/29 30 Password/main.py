from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)

    f_password.delete(0, END)
    f_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = f_website.get()
    user = f_username.get()
    password = f_password.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Don't leave any fields empty")
        return

    message = f"""These are the details you have entered:
    Website: {website}
    user: {user}
    password: {password}"""

    is_ok = messagebox.askokcancel(title="Confirmation", message=message)

    if is_ok:
        row = f"{website}, {user}, {password}\n"
        f_password.delete(0, END)
        f_website.delete(0, END)
        with open("data.txt", mode="a") as handle:
            handle.write(row)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

lb_website = Label(text="Website:")
lb_website.grid(column=0, row=1)
lb_username = Label(text="Email/Username:")
lb_username.grid(column=0, row=2)
lb_password = Label(text="Password:")
lb_password.grid(column=0, row=3)

f_website = Entry(width=45)
f_website.focus()
f_website.grid(column=1, row=1, columnspan=2)
f_username = Entry(width=45)
f_username.insert(0, "micorreo@gmail.com")
f_username.grid(column=1, row=2, columnspan=2)
f_password = Entry(width=33)
f_password.grid(column=1, row=3)

bt_create = Button(text="Make Pass", width=9, command=generate_pass)
bt_create.grid(column=2, row=3)
bt_add = Button(text="Add", width=38, command=save)
bt_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
