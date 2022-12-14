from tkinter import *
import sys
from time import sleep
import tkinter as tk

window=tk.Tk()
Canvas = tk.Canvas(window,width=500, height=200)
Canvas.pack()
oval = Canvas.create_oval(10,10,60,60, fill='blue')
def move_oval():
    Canvas.move(oval, 10, 0)
    Canvas.after(10, move_oval)
move_oval()

root=Tk()
root.title('Cronos A.I')
root.iconbitmap('')
root.geometry("500x350")

# Create an empty string to store the greeting message
greeting = ""

# Concatenate each string in the Greeting list to the greeting variable
Greeting = ["Hello im cronos \n" ,"Im sidehussle's A.I \n", "Lets get started"]
for char in Greeting:
    sleep(0.5)
    greeting += char

# Create a label using the greeting variable as the text
my_label = Label(root, text=greeting, font=("Times-New-Roman",12))
my_label.pack(pady=20)

root.mainloop()
window.mainloop()
