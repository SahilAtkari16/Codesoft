from tkinter import *
import random

root=Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="#87CEEB")

label=Label(root,text="Password generator",font=("Arial",18,"bold"))
label.pack(pady=10)

length_label = Label(root,text="Enter Password Length:",font=("Arial",12),bg="#87CEEB")
length_label.pack()

length_entry = Entry(root, font=("Arial",12))
length_entry.pack(pady=5)

start_type = StringVar()
start_type.set("letter")

Label(root, text="Password should start with:",bg="#87CEEB", font=("Arial", 12)).pack()

Radiobutton(root, text="Number", variable=start_type,value="number", bg="#87CEEB").pack()

Radiobutton(root, text="Uppercase Letter", variable=start_type,value="upper", bg="#87CEEB").pack()

Radiobutton(root, text="Lowercase Letter", variable=start_type,value="lower", bg="#87CEEB").pack()

Radiobutton(root, text="Symbol", variable=start_type,value="symbol", bg="#87CEEB").pack()

def generate_password():
    try:
        characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        length=int(length_entry.get())
        password="".join(random.sample(characters,length))
        password_label.config(text=password)
    except ValueError:
        password_label.config(text="Please enter a valid number")

generate_button=Button(root,text="Generate Password",bg="#171616",fg="white",command=generate_password)
generate_button.pack(pady=10)

password_label=Label(root,text="",font=("Arial",12))
password_label.pack(pady=10)

status_label = Label(root,text="",bg="#87CEEB",font=("Arial",10))
status_label.pack()
status_label.place(x=20, y=350)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(generate_password)
    status_label.config(text="Password copied to clipboard! ✓")
copy_button = Button(root,text="📋 Copy Password",bg="green",fg="white",command=copy_password)
copy_button.pack(pady=5)
root.mainloop()