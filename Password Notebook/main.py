from tkinter import *
from tkinter import messagebox
import random
import  json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for item in range(random.randint(6, 8))]
    password_symbols = [random.choice(symbols) for item in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for item in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # Convert list to string
    password = "".join(password_list)
    pw_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": pw,
        }
    }
    is_empty = len(web) == 0 or len(email) == 0 or len(pw) == 0
    if is_empty:
        messagebox.showinfo(title="Oops", message="Please don't leave an fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)

# ----------------------------- FIND PASSWORD ------------------------------ #


def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

window.config(padx=40, pady=40)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pw_label = Label(text="Password:", width=21)
pw_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)


# focus mouse to the entry
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)

# Set default value
email_entry.insert(0, "changmiao.yu@mail.utoronto.ca")

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

# Button
button_pw = Button(text="Generate Password", width=15, command=generate_password)
button_pw.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)
button_search = Button(text="Search", width=15, command=search)
button_search.grid(column=2, row=1)




window.mainloop()
