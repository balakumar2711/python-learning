from FreeSimpleGUI import ToolTip

import functions

import FreeSimpleGUI as sg #External module

label = sg.Text("Enter an item: ")
input_box = sg.InputText(tooltip="Enter an item", key='todo')
add_button = sg.Button("Add")

window = sg.Window('My app',
                   layout=[[label], [input_box, add_button]],
                   font= ('Arial',10)) #What to display is defined here and the content is managed by Layout

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_fun()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_fun(todos)
        case sg.WIN_CLOSED:
            break

window.close()