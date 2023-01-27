import math
import PySimpleGUI as sg

sg.theme("DarkTeal2")

layout = [
    [sg.Text("Num 1: "), sg.InputText(key="num1")],
    [sg.Text("Num 2: "), sg.InputText(key="num2")],
    [sg.Button("Add"), sg.Button("Subtract"), sg.Button("Multiply"), sg.Button("Divide"), sg.Button("Cancel")]
]

window = sg.Window("Simple Calculator", layout)

event, values = window.read()

while(True):
    if(event == "Add"): # if the add button is pressed
        sg.popup(
            int(values["num1"]) + int(values["num2"]) 
        )
        # can alternativing call a function to do this (if problem is sufficiently complex)
    elif(event == "Subtract"):
        sg.popup(
            int(values["num1"]) - int(values["num2"])
        )
    elif(event == "Multiply"):
        sg.popup(
            int(values["num1"]) * int(values["num2"])
        )
    elif(event == "Divide"):
        sg.popup(
            int(values["num1"]) / int(values["num2"])
        )
    elif(event == "Cancel"):
        break;
    event, values = window.read() # using this to reset event (allowing the user to select another button)

window.close()