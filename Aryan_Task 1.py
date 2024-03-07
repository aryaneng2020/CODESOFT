# Aryan Task 1 To-Do List Using Tkinter

from tkinter import *
from tkinter import messagebox
import tkinter.font

wn = Tk()
wn.title("To-Do List")
wn.iconbitmap('Icon.ico')
wn.minsize(width=400, height=500)
wn.maxsize(width=400, height=500)


# set window color
wn.configure(bg='blue')

# Create an object of type Font from tkinter.
Desired_font = tkinter.font.Font(family="Comic Sans MS",
                                 size=13,
                                 weight="bold")
Desired_font1 = tkinter.font.Font(family="Comic Sans MS",
                                  size=8,
                                  weight="bold")
Desired_font1_list = tkinter.font.Font(family="Comic Sans MS",
                                       size=11,
                                       weight="bold")


# Functions
def add_task():
    if var.get() == "":
        messagebox.showwarning("Warning", "Plz Enter your Task")
    else:
        x = var.get()
        mylist.insert(END, x)
    en.delete(0, 'end')


def rem():
    mylist.delete(ANCHOR)


def edit():
    end_index = mylist.index("end")
    if end_index != 0:
        if var.get() == "":
            messagebox.showwarning("Warning", "Plz Enter your Task")
        else:
            task_index = mylist.curselection()
            if task_index:
                new_task = en.get()
                if new_task:
                    mylist.delete(task_index)
                    mylist.insert(task_index, new_task)
                    en.delete(0, 'end')
            else:
                messagebox.showinfo("Warning", "Select Your Task with which you have to replace it.")
    else:
        messagebox.showinfo("Warning", "ADD Your Task First.")


# Label
lb1 = Label(wn, text='To-Do List', bg="blue", fg="white", font=Desired_font)
lb1.place(x=150, y=0)

lb = Label(wn, text='My Tasks', bg="blue", fg="white", font=Desired_font)
lb.place(x=150, y=80)

# Entry

var = StringVar()
en = Entry(wn, bd='3', textvariable=var, width=40)
en.place(x=30, y=42)

# Button
b1 = Button(wn, text='ADD TASK', bg="Green", fg="white", font=Desired_font1, bd=3, command=add_task)
b1.place(x=300, y=42)

b2 = Button(wn, text="Complete", bg="red", fg="white", font=Desired_font, bd=3, command=rem)
b2.place(x=222, y=400)

b3 = Button(wn, text="Edit my task", bg="Orange", fg="white", font=Desired_font, bd=3, command=edit)
b3.place(x=100, y=400)

# Frame

myframe = Frame(wn, bd=3, relief=RIDGE)
myframe.place(x=50, y=125, width=300, height=250)

# Scroll bar
scr_x = Scrollbar(myframe, orient=HORIZONTAL)
scr_y = Scrollbar(myframe, orient=VERTICAL)

scr_x.pack(side=BOTTOM, fill=X)
scr_y.pack(side=RIGHT, fill=Y)

# List
mylist = Listbox(myframe, font=Desired_font1_list, width=300, height=300, xscrollcommand=scr_x.set,
                 yscrollcommand=scr_y.set)

'''
text='Hurrah!! there is no task left.'
items = ['To buy Grocery', 'HW', 'CW']
for i in items:
    mylist.insert(END, i)
'''
mylist.pack()

# Config
scr_x.config(command=mylist.xview)
scr_y.config(command=mylist.yview)

wn.mainloop()
