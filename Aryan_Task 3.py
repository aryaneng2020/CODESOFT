# Aryan Task 3 Password Generator

import random
import string
import tkinter.font
from tkinter import *
from PIL import ImageTk, Image

wn = Tk()
wn.title("Password Generator")
wn.iconbitmap('pass_Logo.ico')
wn.minsize(width=400, height=400)
wn.maxsize(width=400, height=400)

wn.config(bg="Sky blue")
'''
bg_img = PhotoImage(file="pass_bg.png")

lb4 = Label(wn, image=bg_img)
lb4.place(x=0, y=0, rel width=1, rel height=1)
'''
# Functions

Symbols = """`~!@#$%^&*()_-+={}[]|:;"'<>,.?\\/"""
Poor = string.ascii_uppercase + string.ascii_lowercase
Average = string.digits + string.ascii_uppercase + string.ascii_lowercase
Strong = Poor + Average + Symbols


def passgen():
    if spin_length1.get() == "Poor":
        global check
        check = "".join(random.sample(Poor, it_val.get()))
        lb2.config(text=check)
        return "".join(random.sample(Poor, it_val.get()))
    elif spin_length1.get() == "Average":
        check = "".join(random.sample(Average, it_val.get()))
        lb2.config(text=check)
        return "".join(random.sample(Average, it_val.get()))
    elif spin_length1.get() == "Strong":
        check = "".join(random.sample(Strong, it_val.get()))
        lb2.config(text=check)
        return "".join(random.sample(Strong, it_val.get()))
    else:
        pass


def Copy():
    wn.clipboard_clear()
    wn.clipboard_append(string=check)


# Create an object of type Font from tkinter.
Desired_font = tkinter.font.Font(family="Comic Sans MS",
                                 size=13,
                                 weight="bold")


# Image Resize
img_res = Image.open("pass_Gen.png")
resized = img_res.resize((30, 30), Image.Resampling.LANCZOS)

# image
file = ImageTk.PhotoImage(resized)

# Buttons
b1 = Button(wn, image=file, bd=5, command=passgen, bg="red")
b1.place(x=183, y=300)

b2 = Button(wn, text="Copy to Clipboard", command=Copy, bd=5, bg="light green")
b2.place(x=150, y=340)

# spin box
it_val = IntVar()
spin_length = Spinbox(wn, from_=9, to=25, textvariable=it_val, font=Desired_font, width=5)
spin_length.place(x=225, y=78)

st_var = StringVar()
Strength = ("Strong", "Average", "Poor")
spin_length1 = Spinbox(wn, values=Strength, textvariable=st_var, font=Desired_font, width=10)
spin_length1.pack(padx=(66, 0), pady=(150, 0))

# Labels
lb = Label(wn, text='Password Generator', fg="blue", font=Desired_font, bg="Sky blue")
lb.place(x=120, y=0)

lb1 = Label(wn, text='Select Password Length', fg="blue", font=Desired_font, bg="Sky blue")
lb1.place(x=10, y=80)

lb2 = Label(wn, text="Generated Password", fg="blue", font=Desired_font, justify="center", bg="Sky blue")
lb2.pack(padx=0, pady=(50, 0))

lb3 = Label(wn, text="Select Strength", fg="blue", font=Desired_font, bg="Sky blue")
lb3.place(x=10, y=150)

wn.mainloop()
