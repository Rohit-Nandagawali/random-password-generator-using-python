# tkinter is a built in module use to create window based gui program, this * means we are importing everything from tkinter module

from tkinter import *
import string
import random
import pyperclip

# =========defining functions============
# ==============passwordGenerator=================

def passwordGenerator():
    smallAlphabates = string.ascii_lowercase
    capitalAlphabates = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = smallAlphabates+capitalAlphabates+numbers+special_characters

    # this will take whatever present in string
    password_length = int(length_spinBox.get())


    # password as per radiobuttons
    if choice.get()==1:
        passwordField.insert(0,random.sample(smallAlphabates,password_length))
  
    if choice.get()==2:
        passwordField.insert(0,random.sample(smallAlphabates+capitalAlphabates,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))

    #to generate random password we have to use random module
    # sample(sequence - use to generate password, how much long) 
    # passwordGenerated = random.sample(all,password_length)


# ===========copyToClipboard==========
    # for copying the text we have to install one external module named as 'pyperclip'
def copyToClipboard():
    random_password = passwordField.get()
    # getting copied by copy function
    pyperclip.copy(random_password)
    
# =====================


# this is creating object of the TK class to create window
root=Tk()

# changing background color of the window,bg  argument is used to change the background
# root.config(bg="gray20"

# creating int typr variable for radio buttons
choice = IntVar()

# creating font 
Font = ("arial",15,"bold")

# passwordLableTitle, to create lable we have to create object of the lable class,Lable(where to add,text,font)
passwordLable = Label(root,text="Password Generator",font=("verdana",20,"bold"))

# adding lable to the window
passwordLable.grid()


# ===========================creating radio buttons
# 1 . creating radio button 'weak'
weakRadiobutton = Radiobutton(root,text="weak",value=1,variable=choice,font=Font)

# adding radiobutton to the window, pady will adding padding of 5 vertically
weakRadiobutton.grid(pady=5)

# 2 . creating radio button 'medium'
mediumRadiobutton = Radiobutton(root,text="medium",value=2,variable=choice,font=Font)

# adding radiobutton to the window
mediumRadiobutton.grid(pady=5)

# 3 . creating radio button 'strong'
strongRadiobutton = Radiobutton(root,text="strong",value=3,variable=choice,font=Font)

# adding radiobutton to the window
strongRadiobutton.grid(pady=5)

# ===============
# passwordLengthLable, to create lable we have to create object of the lable class,Lable(where to add,text,font)
passwordLengthLable = Label(root,text="Password Length",font=Font)

# adding lable to the window
passwordLengthLable.grid()


#=========creating a spinner
length_spinBox = Spinbox(root,from_=5,to_=18,width=5,font=Font)
# adding spinner
length_spinBox.grid()

# ===========creating button to generate
generateButton = Button(root,text="Generate ",font=Font,command=passwordGenerator)
generateButton.grid(pady=5)

# =============input fied for showing generated password, bd=>border
passwordField = Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

# ===========creating button to copy
copyButton = Button(root,text="copy",font=Font,command=copyToClipboard)
copyButton.grid(pady=5)


# this will keep our window on a loop,this will keep our window visile
root.mainloop()