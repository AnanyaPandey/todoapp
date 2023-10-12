import PySimpleGUI as sg
import todoapp_functions

label = sg.Text("Here is the todo list")
inputbox = sg.InputText(tooltip="Enter a todo item",
                        key='item')
addbutton = sg.Button("Add")

window = sg.Window(title="My to-do App",
                   layout=[[label],[inputbox,addbutton]],
                   font = ('Helvetica',14)) # must be list of lists

# with While loop the app will not close on clicking add button
# it will jeep on printing values on clicking add button

while True:

    event,value = window.read() # Returns the text written no input box along with other variables
    # ('Add', {todo:'Hi'}) this is the format in which this returns the value
    # on pressing the add button the app exited and returned this
    print(event) # Add
    print(value) # {todo:'Hi}
    if event == "Add":
        todos = todoapp_functions.get_todos('todoapp.txt')
        new_todo = value['item'] + '\n'
        todos.append(new_todo)
        todoapp_functions.save_todos(todos)
    elif event == sg.WIN_CLOSED :
        break
window.close()
