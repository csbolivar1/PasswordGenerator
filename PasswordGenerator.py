from tkinter import *
import random
import string
import time

root = Tk()

def generatePassword():
    copyConfirm.config(text="") # TODO: temp solution, should be in copyPassword function
    password = ''.join(random.choice(string.ascii_letters) for x in range(clicked.get()))
    passwordLabel.config(text=password)

def copyPassword():
    root.clipboard_clear()
    root.clipboard_append(passwordLabel['text'])
    copyConfirm.config(text="Password Copied")
    
    
passwordLabel = Label(root, text="filler")                       
generatePasswordBtn = Button(root, text="Generate Password", command=generatePassword)
copyPasswordBtn = Button(root, text="Copy Password", command=copyPassword)
copyConfirm = Label(root, text="")

clicked = IntVar()
clicked.set(5)

upperCaseChkBtn = Checkbutton(root, text="Include Uppercase Letters (A-Z)")
lowerCaseChkBtn = Checkbutton(root, text="Include Lowercase Letters (a-z)")
numberChkBtn = Checkbutton(root, text="Include Numbers (0-9)")
specialCharChkBtn = Checkbutton(root, text="Include Special Characters")
passwordLength = OptionMenu(root, clicked, 5, 6, 7, 8, 9, 10)

passwordLabel.pack()
generatePasswordBtn.pack()
copyPasswordBtn.pack()
copyConfirm.pack()
upperCaseChkBtn.pack()
lowerCaseChkBtn.pack()
numberChkBtn.pack()
specialCharChkBtn.pack()
passwordLength.pack()

root.mainloop()