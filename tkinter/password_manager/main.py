from tkinter import messagebox
from tkinter import *
import random
import pyperclip
import json


def add_passwrd_to_doc():

    name = entry_name.get()
    passw = entry_passwrd.get()
    us_name = entry_user.get()
    new_dict = {
        name: {
            "email": us_name,
            "password": passw,
        }
    }

    if len(name) != 0 and len(passw) != 0:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_dict, file, indent=4)
        else:
            data.update(new_dict)

            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        finally:
            entry_name.delete(0, END)
            entry_passwrd.delete(0, END)
    else:
        messagebox.showinfo(title="Error", message="Insert all demanded information")


def generate_new_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    rand_pass = "".join(password_list)

    entry_passwrd.insert(0, rand_pass)
    pyperclip.copy(rand_pass)


def find_pass():
    name = entry_name.get()
    try:
        with open("data.json", mode="r") as check_file:
            data = json.load(check_file)
            if name in data:
                value = data.get(name)
                messagebox.showinfo(title="information requested",
                                    message=f"Username/email: {value['email']}\n Password: {value['password']}")
            else:
                messagebox.showinfo(title="Error", message="Not saved yet.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Nothing saved in database yet.")


window = Tk()

window.title("Password Manager")
window.config(height=500, width=600, bg="white", padx=20, pady=20)

website_name = Label(text="Website: ")
website_name.grid(column=0, row=1)
entry_name = Entry(width=35)
entry_name.focus()
entry_name.grid(column=1, row=1, columnspan=2)

user_name = Label(text="Email/Username: ")
user_name.grid(column=0, row=2)
entry_user = Entry(width=35)
entry_user.grid(column=1, row=2, columnspan=2)
entry_user.insert(0, "giannikleiss4@gmail.com")

passwrd = Label(text="Password: ")
passwrd.grid(column=0, row=3)
entry_passwrd = Entry(width=26)
entry_passwrd.grid(column=1, row=3)

button_add_passwrd = Button(text="Generate Password", command=generate_new_pass)
button_add_passwrd.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command=add_passwrd_to_doc)
add_button.grid(column=1, row=4)

button_search = Button(text="Search", width=15, command=find_pass)
button_search.grid(column=3, row=1, columnspan=2)

canvas = Canvas(width=200, height=240, bg="white", highlightthickness=0)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100, 114, image=canvas_image)
canvas.grid(column=1, row=0)

window.mainloop()
