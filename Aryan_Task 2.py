# Aryan Task 2 Calculator

from tkinter import *


def click(event):
    global svar
    text = event.widget.cget("text")
    if text == "=":
        if svar.get().isdigit():
            value = int(svar.get())
        else:
            value = eval(svar.get())
        svar.set(value)
        scanEntry.update()
    elif text == "All Clear":
        svar.set("")
        scanEntry.update()

    else:
        svar.set(svar.get() + text)
        scanEntry.update()


root = Tk()
root.title("Calculator")
root.maxsize(width=500, height=600)
root.minsize(width=500, height=600)

root.wm_iconbitmap("favicon.ico")

svar = StringVar()
svar.set("")
scanEntry = Entry(root, textvariable=svar, font="lucid 40 bold", bg="light gray")
scanEntry.pack(fill=X, padx=10, pady=10, ipadx=8)

f1 = Frame(root, bg="gray")

b = Button(f1, text="9", font="lucid 30 bold ", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="8", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="7", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="/", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="gray")
b = Button(f1, text="6", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="5", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)
b = Button(f1, text="4", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="*", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="gray")
b = Button(f1, text="3", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="2", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)
b = Button(f1, text="1", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="-", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="gray")
b = Button(f1, text="0", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text=".", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=30, pady=8)
b.bind("<Button-1>", click)
b = Button(f1, text="=", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="+", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=23, pady=8)
b.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root, bg="gray")

b = Button(f1, text="All Clear", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=45, pady=8)
b.bind("<Button-1>", click)

b = Button(f1, text="%", font="lucid 30 bold", pady=5, padx=15)
b.pack(side=LEFT, padx=45, pady=8)
b.bind("<Button-1>", click)

f1.pack()

root.mainloop()
