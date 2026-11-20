# Import necessary libraries

from tkinter import *

from datetime import date

# Create a window

root = Tk()

root.title('Getting started with Widgets')

root.geometry('400x300')

# Add label

lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=30)

# Label for getting name as input

name_lbl = Label(text="Full Name", bg="#3895D3")

# Entry widget

name_entry = Entry()

# Text widget to display information

text_box = Text(height=5, width=40)

# Function to display a message

def display():

    # Read input given by user

    name = name_entry.get()

    # Create welcome message

    message = "Welcome to the Application!\nToday's date is: "

    greet = "Hello " + name + "\n"

    # Display details inside the text box

    text_box.delete("1.0", END)

    text_box.insert(END, greet)

    text_box.insert(END, message)

    text_box.insert(END, str(date.today()))

# Add button

btn = Button(

text="Begin",

command=display,

height=1,

bg="#1261A0",

fg="white"

)

# Organize widgets

lbl.pack()

name_lbl.pack()

name_entry.pack()

btn.pack()

text_box.pack()

# Start GUI event loop

root.mainloop()

