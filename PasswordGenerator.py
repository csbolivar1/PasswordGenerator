from tkinter import *
import random
import string

root = Tk()
root.title("Password Generator")
root.geometry("280x250")
root.minsize(280, 250)
root.maxsize(280, 250)
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
    
passwordLabel = Label(root, text=password.join(random.choice(string.ascii_letters) for x in range(clicked.get())), font=(50))                       
generatePasswordBtn = Button(root, text="Generate Password", command=generatePassword, padx=20, font=(50))
copyPasswordBtn = Button(root, text="Copy Password", command=copyPassword, padx=34, font=(50))
copyConfirm = Label(root, text="", font=(50))

numberChkBtn = Checkbutton(root, text="Include Numbers (0-9)", variable=numchk, onvalue=1, offvalue=0, font=(50))
specialCharChkBtn = Checkbutton(root, text="Include Special Characters", variable=spcheck, onvalue=1, offvalue=0, font=(50))
passwordLength = OptionMenu(root, clicked, 8, 9, 10, 11, 12, 13, 14, 15)
passwordLength.config(font=50)
passwordLengthLabel = Label(root, text="Password Length:", font=(50))

passwordLabel.pack()
generatePasswordBtn.pack()
copyPasswordBtn.pack()
copyConfirm.pack()
passwordLengthLabel.pack()
passwordLength.pack()
numberChkBtn.pack()
specialCharChkBtn.pack()

root.mainloop()