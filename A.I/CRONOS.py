# Import module 
from tkinter import *
import customtkinter
import tkinter
import tkinter.messagebox
import time,os,sys

#definitions
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")

#setting up theme
customtkinter.set_appearance_mode("system")

#setting up theme for components
customtkinter.set_default_color_theme("blue")
  
# Create ctk window 
root = customtkinter.CTk()
  
# Adjust size 
root.geometry("400x400")
  
#CTK Buttons
Button=customtkinter.CTkRadioButton(master=root, typingPrint("Hello im  Cronos/n"), time.sleep(1), typingPrint("Im Sidehussles little A.I"), time.sleep(1), typingPrint("click on the circle to get started"))

#show at center of screen
Button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Execute tkinter
root.mainloop()