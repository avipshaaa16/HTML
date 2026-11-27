#Import necessary libraries
from tkinter import *
import tkinter.messagebox

#Create a window
root = Tk()
root.geometry("200x200")

#function for displaying warning message
#this will be called once the button is clicked
#messagebox.showwarning("Window Name" , "Text to be displayed")
def msg():
    tkinter.messagebox.showwarning("Alert", "Stop! Virus Found")

#adding button widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

#entering main event loop
root.mainloop()
