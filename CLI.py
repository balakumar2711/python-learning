import functions

while True:
    """
    Input the entry and strip any blank spaces
    at the end if it is present
    """
    todo = input("Enter add, show/display, edit,complete or exit:")
    todo = todo.strip() #Incase if unknowingly some spaces gets added

    if todo.startswith("add"):
       """
       Using the index to identify items starting with 
       add and then removing the item next to it and adding
       to the text file using read and write functions
       """
       name = todo[4:]

       todos = functions.read_fun()

       todos.append(name + '\n')

       functions.write_fun(todos)

    elif todo.startswith('show') or todo.startswith('display'):
        """
        Using the startwith function to identify items starting 
        with show/display and using the read file to display
        the list
        """
        todos = functions.read_fun()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif todo.startswith('edit'):
        """
        Using the start with function to identify items starting 
        with edit and then editing the item and adding with
        required item using read and write functions.
        
        Try and except is used to catch the errors when the input 
        is provided wrongly
        """
        try:
            number = int(todo[5:])
            number = number - 1

            todos = functions.read_fun()

            new_item = input("Enter the new item: ")
            todos[number] = new_item + '\n'

            functions.write_fun(todos)

        except IndexError:
            print("There is no item with that number.")
            continue

        except ValueError:
            print("Enter a valid number after the edit function.")
            continue

    elif todo.startswith('complete'): #Adding a remove/pop method
        """
        Using the start with function to identify items starting 
        with complete and then removing the item and modifying the file
        using read and write functions.

        Try and except is used to catch the errors when the input 
        is provided wrongly
        """
        try:
            number = int(todo[9:])

            todos = functions.read_fun()

            index = number-1
            item_to_remove = todos[index].strip()
            todos.pop(index)

            functions.write_fun(todos)

            print(f"The item {item_to_remove} has been removed")

        except IndexError:
            print("There is no item with that number.")
            continue

        except ValueError:
            print("Enter a valid number after the complete function.")
            continue

    elif todo.startswith('exit'):
        break

    else:
        print("This isn't an expected input")

print("Ciao!")