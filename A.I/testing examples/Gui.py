from tkinter import *
import sys
from time import sleep

root=Tk()
root.title('Cronos A.I')
root.iconbitmap('')
root.geometry("500x350")

Greeting = ["Hello im cronos \n" ,"Im sidehussle's A.I \n", "Lets get started"]
for char in Greeting:
    sleep(0.5)
    x=sys.stdout.write(char)

greet=x


my_label = Label(root, text=greet, font=("Times-New-Roman",12))
my_label.pack(pady=20)

root.mainloop()