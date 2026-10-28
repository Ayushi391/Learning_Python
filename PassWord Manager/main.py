from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','R','S','T','U','V','W','X','Y','Z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','#','$','%','&','(',')','*','+']
    #list comprehension
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    result= password_letter + password_symbol + password_numbers
    shuffle(result)
    password="".join(result)
    pass_entry.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# f = open("data.txt", "x")
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password
        }
    }

    if len(website)== 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please do not leave any field empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else: 
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD --------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data:
            messagebox.showinfo(message=f"Website: {website}\nPassword: {data[website]["password"]}")
        else: 
            messagebox.showinfo(title="Error", message=f"No detail for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column=1, row=0)

#website label
website = Label(text="Website : ")
website.grid(column=0, row=1)

#website textbox
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()

#search button
search = Button(text="Search", width=14, command= find_password)
search.grid(row=1, column=2)

#Email label
email = Label(text="Email/Username : ")
email.grid(column=0, row=2)

#email textbox
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "aushi@gmail.com")

#password label
password = Label(text="Password : ")
password.grid(column=0, row=3)

#password entry
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky="w")

#generate password button
pass_button = Button(text="Generate Password", command=generate_pass)
pass_button.grid(column=2, row=3, sticky="w")

#add button
add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
