from tkinter import *
import random
import string

root = Tk()
password = ''

clicked = IntVar()
clicked.set(5)

numchk = IntVar()

def generatePassword():
    copyConfirm.config(text="") # TODO: temp solution, should be in copyPassword function
    password = ''.join(random.choice(string.ascii_letters) for x in range(clicked.get()))

    # TODO: add numbers to password generation

    if numchk.get() == 1:
        password = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(clicked.get()))

    passwordLabel.config(text=password)

def copyPassword():
    root.clipboard_clear()
    root.clipboard_append(passwordLabel['text'])
    copyConfirm.config(text="Password Copied")
    
passwordLabel = Label(root, text=password.join(random.choice(string.ascii_letters) for x in range(clicked.get())))                       
generatePasswordBtn = Button(root, text="Generate Password", command=generatePassword)
copyPasswordBtn = Button(root, text="Copy Password", command=copyPassword)
copyConfirm = Label(root, text="")

numberChkBtn = Checkbutton(root, text="Include Numbers (0-9)", variable=numchk, onvalue=1, offvalue=0)
# specialCharChkBtn = Checkbutton(root, text="Include Special Characters")
passwordLength = OptionMenu(root, clicked, 5, 6, 7, 8, 9, 10)

passwordLabel.pack()
generatePasswordBtn.pack()
copyPasswordBtn.pack()
copyConfirm.pack()
numberChkBtn.pack()
# specialCharChkBtn.pack()
passwordLength.pack()

root.mainloop()