from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def generate_password():
    letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','#','$','%','^','&','*','(',')','+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_numbers+password_symbols+password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0 or len(email)==0 :
        messagebox.showinfo(title="Oops...", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Website: {website}\n Email: {email}\n Password: {password}\nIs it ok to save?")
        if is_ok:
            with open('data.txt', mode='a') as password_file:
                password_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='./lock.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row= 1, column=0)
email_label.grid(row=2 , column=0)
password_label.grid(row=3 , column=0)

website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.grid(row= 1, column=1, columnspan=2, sticky="EW")
email_entry.grid(row= 2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row= 3, column=1, columnspan=1, sticky="EW")

website_entry.focus()
email_entry.insert(0, 'singhakashkumar.a@gmail.com')

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4,column=1,columnspan=2, sticky="EW")

window.mainloop()
