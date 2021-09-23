from tkinter import *
import random
import string

root = Tk()
password = ''

clicked = IntVar()
clicked.set(8)

numchk = IntVar()
spcheck = IntVar()

def generatePassword():
    copyConfirm.config(text="") # TODO: temp solution, should be in copyPassword function
    password = ''.join(random.choice(string.ascii_letters) for x in range(clicked.get()))

    if numchk.get() == 1:
        password = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(clicked.get()))

    if spcheck.get() == 1:
        password = ''.join(random.choice(string.ascii_letters + string.punctuation) for x in range(clicked.get()))

    passwordLabel.config(text=password)

def copyPassword():
    root.clipboard_clear()
    root.clipboard_append(passwordLabel['text'])
    copyConfirm.config(text="Password Copied")
    
passwordLabel = Label(root, text=password.join(random.choice(string.ascii_letters) for x in range(clicked.get())))                       
generatePasswordBtn = Button(root, text="Generate Password", command=generatePassword, padx=20)
copyPasswordBtn = Button(root, text="Copy Password", command=copyPassword, padx=29)
copyConfirm = Label(root, text="")

numberChkBtn = Checkbutton(root, text="Include Numbers (0-9)", variable=numchk, onvalue=1, offvalue=0)
specialCharChkBtn = Checkbutton(root, text="Include Special Characters", variable=spcheck, onvalue=1, offvalue=0)
passwordLength = OptionMenu(root, clicked, 8, 9, 10, 11, 12, 13, 14, 15)
passwordLengthLabel = Label(root, text="Password Length:")


passwordLabel.grid(row=0, column=0)
generatePasswordBtn.grid(row=1, column=0)
copyPasswordBtn.grid(row=2, column=0)
copyConfirm.grid(row=3, column=0)
passwordLengthLabel.grid(row=4, column=0)
passwordLength.grid(row=5, column=0)
numberChkBtn.grid(row=6, column=0)
specialCharChkBtn.grid(row=7, column=0)

root.mainloop()