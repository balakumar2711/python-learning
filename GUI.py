from FreeSimpleGUI import ToolTip

import functions

import FreeSimpleGUI as sg #External module

label = sg.Text("Enter an item: ")
input_box = sg.InputText(tooltip="Enter an item", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_fun(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')

window = sg.Window('My app',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
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
            window['todos'].update(values=todos) #Add the item in real time in the GUI

        case 'Edit':
            todo_to_edit = values['todos'][0] #This gives the string that I want to edit.
            new_todo = values['todo'] + '\n' #This gets the value from the input box which is where I have entered my new item

            todos = functions.read_fun() #Read the existing list
            index = todos.index(todo_to_edit) #Get the index of the selected item
            todos[index] = new_todo #Modify the list to add the new item
            functions.write_fun(todos)
            window['todos'].update(values=todos) #Access the list box(Window is the parent here) and update the values to latest so that in real time in GUI you will get the updated list

        case 'todos': #Right now if this is not specified everytime when a item is selected for replacing its not updating in the input box to reflect the selection
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()