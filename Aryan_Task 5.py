from tkinter import *
import csv
from tkinter import messagebox

phonelist = []


def ReadCSVFile():
    global header
    with open('StudentData.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            phonelist.append(row)
    print(phonelist)
    set_select()


def WriteInCSVFile(phonelist):
    with open('StudentData.csv', 'w', newline='') as csv_file:
        writeobj = csv.writer(csv_file, delimiter=',')
        writeobj.writerow(header)
        for row in phonelist:
            writeobj.writerow(row)


def WhichSelected():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def AddDetail():
    if E_name.get() != "" and E_Email.get() != "" and E_contact.get() != "" and E_address.get() != "":
        phonelist.append([E_name.get() , E_Email.get(), E_contact.get(),E_address.get()])
        print(phonelist)
        WriteInCSVFile(phonelist)
        set_select()
        EntryReset()
        messagebox.showinfo("Confermation", "Succesfully Add New Contact")

    else:
        messagebox.showerror("Error", "Please fill the information")


def UpdateDetail():
    if E_name.get() and E_Email.get() and E_contact.get() and E_address.get():
        phonelist[WhichSelected()] = [E_name.get() , E_Email.get(), E_contact.get(),E_address.get()]
        WriteInCSVFile(phonelist)
        messagebox.showinfo("Confirmation", "Succesfully Update Contact")
        EntryReset()
        set_select()

    elif not (E_name.get()) and not (E_Email.get()) and not (E_contact.get()) and not (E_address.get()) and not (
            len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill the information")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """
            messagebox.showerror("Error", message1)


def EntryReset():
    E_name_var.set('')
    E_Email_var.set('')
    E_contact_var.set('')
    E_address_var.set('')

def DeleteEntry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result == True:
            del phonelist[WhichSelected()]
            WriteInCSVFile(phonelist)
            set_select()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def LoadEntry():
    name,email,phone,address = phonelist[WhichSelected()]
    #print(name.split(' '))
    E_name_var.set(name)
    #E_Email_var.set(name.split()[1])
    E_Email_var.set(email)
    E_contact_var.set(phone)
    E_address_var.set(address)

def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i = 0
    for name, email, phone, address in phonelist:
        i += 1
        select.insert(END, f"{i}  |   {name}  |  {email}  |   {phone}  |   {address}")


window = Tk()
window.wm_iconbitmap("Contact_list.ico")
window.title("Contact list")
Frame1 = LabelFrame(window, text="Enter the Contact Detail")
Frame1.grid(padx=15, pady=15)

Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0, column=0, padx=15, pady=15)
# ---------------------------------------------
l_name = Label(Inside_Frame1, text="Name")
l_name.grid(row=0, column=0, padx=5, pady=5)
E_name_var = StringVar()

E_name = Entry(Inside_Frame1, width=30, textvariable=E_name_var)
E_name.grid(row=0, column=1, padx=5, pady=5)
# -----------------------------------------------
l_Email = Label(Inside_Frame1, text="Email")
l_Email.grid(row=1, column=0, padx=5, pady=5)
E_Email_var = StringVar()
E_Email = Entry(Inside_Frame1, width=30, textvariable=E_Email_var)
E_Email.grid(row=1, column=1, padx=5, pady=5)
# ---------------------------------------------------
l_contact = Label(Inside_Frame1, text="Contact")
l_contact.grid(row=2, column=0, padx=5, pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1, width=30, textvariable=E_contact_var)
E_contact.grid(row=2, column=1, padx=5, pady=5)
# ---------------------------------------------------
l_address = Label(Inside_Frame1, text="Address")
l_address.grid(row=3, column=0, padx=5, pady=5)
E_address_var = StringVar()
E_address = Entry(Inside_Frame1, width=30, textvariable=E_address_var)
E_address.grid(row=3, column=1, padx=5, pady=5)
# ---------------------------------------------------
Frame2 = Frame(window)
Frame2.grid(row=0, column=1, padx=15, pady=15, sticky=E)
# <><><><><><><><><><><><><><<><<<><><<<><><><><><><><><><>
Add_button = Button(Frame2, text="Add Detail", width=15, bg="#6B69D6", fg="#FFFFFF", command=AddDetail)
Add_button.grid(row=0, column=0, padx=8, pady=8)

Update_button = Button(Frame2, text="Update Detail", width=15, bg="#6B69D6", fg="#FFFFFF", command=UpdateDetail)
Update_button.grid(row=1, column=0, padx=8, pady=8)

Reset_button = Button(Frame2, text="Reset", width=15, bg="#6B69D6", fg="#FFFFFF", command=EntryReset)
Reset_button.grid(row=2, column=0, padx=8, pady=8)
# ----------------------------------------------------------------------------

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1, column=0, padx=15, pady=15)

scroll_y = Scrollbar(DisplayFrame, orient=VERTICAL)
scroll_x= Scrollbar(DisplayFrame, orient=HORIZONTAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, font=("Arial Bold", 10), bg="#282923", fg="#E7C855", width=40,
                 height=10, borderwidth=3, relief="groove")
scroll_y.config(command=select.yview)
scroll_x.config(command=select.xview)
select.grid(row=0, column=0, sticky=W)
scroll_y.grid(row=0, column=1, sticky=N + S)
scroll_x.grid(row=1, column=0, sticky=E + W)
# -----------------------------------------------------------------------------------
ActionFrame = Frame(window)
ActionFrame.grid(row=1, column=1, padx=15, pady=15, sticky=E)

Delete_button = Button(ActionFrame, text="Delete", width=15, bg="#D20000", fg="#FFFFFF", command=DeleteEntry)
Delete_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)

Loadbutton = Button(ActionFrame, text="Load", width=15, bg="#6B69D6", fg="#FFFFFF", command=LoadEntry)
Loadbutton.grid(row=1, column=0, padx=5, pady=5)
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

ReadCSVFile()

window.mainloop()