from tkinter import *
import random
import string

root = Tk()
root.title("Password Generator")
root.geometry("280x250")
root.minsize(280, 250)
root.maxsize(280, 250)

passwordLength = IntVar()
passwordLength.set(8)

numCheck = IntVar()
spCheck = IntVar()

password = ''

# Creates password
def generatePassword():
    copyConfirm.config(text="") 
    password = ''.join(random.choice(string.ascii_letters) for x in range(passwordLength.get()))

    if numCheck.get() == 1:
        password = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(passwordLength.get()))

    if spCheck.get() == 1:
        password = ''.join(random.choice(string.ascii_letters + string.punctuation) for x in range(passwordLength.get()))

    passwordLabel.config(text=password)

# Copy generated password to clipboard
def copyPassword():
    root.clipboard_clear()
    root.clipboard_append(passwordLabel['text'])
    copyConfirm.config(text="Password Copied")
    
# Required labels
passwordLabel = Label(root, text=password.join(random.choice(string.ascii_letters) for x in range(passwordLength.get())), font=(50))                       
generatePasswordBtn = Button(root, text="Generate Password", command=generatePassword, padx=20, font=(50))
copyPasswordBtn = Button(root, text="Copy Password", command=copyPassword, padx=34, font=(50))
copyConfirm = Label(root, text="", font=(50))
numberChkBtn = Checkbutton(root, text="Include Numbers (0-9)", variable=numCheck, onvalue=1, offvalue=0, font=(50))
specialCharChkBtn = Checkbutton(root, text="Include Special Characters", variable=spCheck, onvalue=1, offvalue=0, font=(50))
passwordLengthSelect = OptionMenu(root, passwordLength, 8, 9, 10, 11, 12, 13, 14, 15)
passwordLengthSelect.config(font=50)
passwordLengthLabel = Label(root, text="Password Length:", font=(50))

# Place labels in window
passwordLabel.pack()
generatePasswordBtn.pack()
copyPasswordBtn.pack()
copyConfirm.pack()
passwordLengthLabel.pack()
passwordLengthSelect.pack()
numberChkBtn.pack()
specialCharChkBtn.pack()

root.mainloop()