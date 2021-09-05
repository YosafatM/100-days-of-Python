from tkinter import *

TITLE = "Mile to Km converter"
TEXT_IS_EQUAL = "is equal"
TEXT_KM = "Km"
TEXT_MILES = "Miles"
TEXT_CALCULATE = "Calculate"


def converter():
    try:
        miles = float(field.get())
        km = miles * 1.60934
        label_result["text"] = km
    except ValueError:
        label_result["text"] = "NAN"


window = Tk()
window.title(TITLE)
window.config(padx=30, pady=30)

# First row
field = Entry()
field.grid(column=1, row=0)

label_miles = Label(text=TEXT_MILES)
label_miles.grid(column=2, row=0)

# Second row
label_equivalent = Label(text=TEXT_IS_EQUAL)
label_equivalent.grid(column=0, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

label_km = Label(text=TEXT_KM)
label_km.grid(column=2, row=1)

# Third row
button_calc = Button(text=TEXT_CALCULATE, command=converter)
button_calc.grid(column=1, row=2)

window.mainloop()
