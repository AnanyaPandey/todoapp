import PySimpleGUI as sg
import todoapp_functions

label = sg.Text("Here is the todo list")
inputbox = sg.InputText(tooltip="Enter a todo item",
                        key='item')
addbutton = sg.Button("Add")
listbox = sg.Listbox(values=todoapp_functions.get_todos(),
                     key="listoftodos",
                     enable_events=True,
                     size=[30,20])

editbutton = sg.Button("Edit")
window = sg.Window(title="My to-do App",
                   layout=[[label],
                           [inputbox,addbutton],
                           [listbox,editbutton]],
                   font = ('Helvetica',14)) # must be list of lists

# with While loop the app will not close on clicking add button
# it will keep on printing values on clicking add button

while True:

    event,value = window.read() # Returns the text written no input box along with other variables
    # ('Add', {todo:'Hi'}) this is the format in which this returns the value
    # on pressing the add button the app exited and returned this
    print(event) # Add
    print(type(value))
    print(value) # {todo:'Hi}
    print(value['listoftodos'])
    if event == "Add":
        todos = todoapp_functions.get_todos('todoapp.txt')
        new_todo = value['item'] + '\n'
        todos.append(new_todo)
        todoapp_functions.save_todos(todos)
    elif event == 'Edit':
        todo_to_edit = value['listoftodos'][0]
        new_todo = value['item']

        todos=todoapp_functions.get_todos()
        index_to_replace = todos.index(todo_to_edit)
        todos[index_to_replace] = new_todo
        todoapp_functions.save_todos(todos)

        window['listoftodos'].update(values=todos)
    elif event == sg.WIN_CLOSED :
        break
window.close()
