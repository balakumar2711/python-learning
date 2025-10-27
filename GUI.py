import functions

import FreeSimpleGUI as sg #External module

label = sg.Text("Enter an item: ")
input_box = sg.InputText()
add_button = sg.Button("Add")

window = sg.Window('My app', layout=[[label], [input_box, add_button]]) #What to display is defined here and the content is managed by Layout
window.read()
window.close()