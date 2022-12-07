# Import module 
from tkinter import *
import customtkinter
import tkinter
import tkinter.messagebox
import time,os,sys

#setting up theme
customtkinter.set_appearance_mode("system")

#setting up theme for components
customtkinter.set_default_color_theme("blue")
  
# Create ctk window 
root = customtkinter.CTk()
  
# Adjust size 
root.geometry("400x400")
  
#CTK Buttons
Button=customtkinter.CTkRadioButton(master=root, text="")

#show at center of screen
Button.place(relx=0.5, rely=0.5, anchor=CENTER)

#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
import time,os,sys

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
    
typingPrint("Hello im Cronos\n")
time.sleep(1)
typingPrint("sidehussle's A.I\n")
time.sleep(1)

pillColor = typingInput("Need Help job finidng? (Type Y for Yes, N for No)")

if pillColor == "Y":
  typingPrint("Initiating job finding sequence protocol ")
  typingPrint("your results are minuts away\n")
elif pillColor == "N":
  typingPrint("Are you Hiring ")
  typingPrint("Type E for employer\n")
else:
  typingPrint("Invalid answer!")

# Execute tkinter
root.mainloop()