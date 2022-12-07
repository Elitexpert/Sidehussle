#Cronos.py#
import PySimpleGUI as sg

layout = [[sg.Text("Cronos AI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

#create background image


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()