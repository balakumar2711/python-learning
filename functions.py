def read_fun(filename="todos.txt"):
    """
    Read a text file and return the list
    of todo items
    """
    with open(filename, "r") as file_fun:
        todos_fun = file_fun.readlines()
    return todos_fun

def write_fun(todos_arg, filename="todos.txt"): #Passing variables in the write function but here return is not needed since it processes the file and write to it
    """
    Open the read text file and write the appended
    text to the text file
    """
    with open(filename, "w") as file_local:
        file_local.writelines(todos_arg)