# Import module 
from tkinter import *
import customtkinter

#setting up theme
customtkinter.set_appearance_mode("system")

#setting up theme for components
customtkinter.set_default_color_theme("blue")
  
# Create ctk window 
root = customtkinter.CTk()
  
# Adjust size 
root.geometry("400x400")
  
#CTK Buttons
Button=customtkinter.CTkRadioButton(master=root, text="Hi im Cronos . Sidehussles Helper")

#show at center of screen
Button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Execute tkinter
root.mainloop()