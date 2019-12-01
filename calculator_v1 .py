# Import the Tkinter module
from tkinter import *

# Initialize the window
root = Tk()

# Create the title
root.title("Simple Calculator")

# Create and size the entry window
e = Entry(root,width=30,borderwidth=5)
e.grid(row=0,columnspan=3)


def button_click(number):
    '''This function makes it possible for the Entry screen to properly display the
        proper number in the order that it was entered'''
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))


def button_clear():
    '''This function will run whenever the C button is clicked and
        it will delete whatever is the in Entry window'''
    e.delete(0,END)

def button_add():
    '''This function will retrieve whatever is in the Entry window, store
        it in the first_number variable , then it defines the global variable
        f_num so we are able to grab the f_num from another function, then the function
        assigns the number we grabbed from the Entry window to the global variable and deletes
        anything in the box to get ready for the next input number'''
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    '''This function grabs the second number that is typed into the Entry window
        and then deletes the second number to make room for the answer to be inserted into the
        Entry window'''
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0,f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0,f_num * int(second_number))
    elif math == "division":
        e.insert(0,f_num // int(second_number))












number0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0)).grid(row=4,column=0)
number1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1)).grid(row=3,column=2)
number2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2)).grid(row=3,column=1)
number3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3)).grid(row=3,column=0)
number4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4)).grid(row=2,column=2)
number5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5)).grid(row=2,column=1)
number6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6)).grid(row=2,column=0)
number7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7)).grid(row=1,column=2)
number8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8)).grid(row=1,column=1)
number9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9)).grid(row=1,column=0)




add_button = Button(root,text="+",padx=40,pady=20,command=button_add).grid(row=5,column=0)
multiply_button = Button(root,text="*",padx=40,pady=20,command=button_multiply).grid(row=6,column=0)
divide_button = Button(root,text="/",padx=40,pady=20,command=button_divide).grid(row=6,column=1)
subtract_button = Button(root,text="-",padx=40,pady=20,command=button_subtract).grid(row=5,column=1)
equal_button = Button(root,text="=",padx=40,pady=20,command=button_equal).grid(row=7,column=1)
clear_screen_button = Button(root,text="C",padx=40,pady=20,command=button_clear).grid(row=7,column=0)


root.mainloop()
