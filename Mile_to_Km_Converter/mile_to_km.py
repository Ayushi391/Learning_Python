# Mile to Kilometer Converter
from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

#--the mile value
number_entry = Entry(window, width=10)
number_entry.grid(column=1, row=0)

#--mile label
label = Label(text=" Miles")
label.grid(column=2, row=0)

#--km text label
text = Label(text=" is equal to")
text.grid(column=0, row=1)

#--km label
label2 = Label(text=" Km")
label2.grid(column=2, row=1)

#--converted value, calculate button
def convert():
    mile_value = float(number_entry.get())
    km_value = round(mile_value* 1.609344)
    km_text = Label(text=0)
    km_text.config(text= km_value)
    km_text.grid(column=1, row=1)

button = Button(text="Calculate" , command=convert)
button.grid(column=1, row=2)

window.mainloop()