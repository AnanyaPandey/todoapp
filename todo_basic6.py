# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:55:25 2023

@author: pandey

Version 1.5
* Directly Add the item with add option
* Separate show function to use multiple time whenever necessary
* Fixed the bug - add did not had \n
* Use Functions to separate actions within program

"""
def showtodolist(todos):
    '''
    Parameters
    ----------
    todos : list of todo items 
    
    The function takes input the list that it needs to display
    the function creates a temporary list which has all new line characters
    stripped and then shows tht temp list for user to interact with.
    
    Returns
    -------
    None.
    
    '''
    newtodos = [item.strip('\n') for item in todos]
    for i,item in enumerate(newtodos):
        print(f"{i+1}-{item}")
    
def get_todos(todosfilepath):
    
    todos = []  #todos must be a list 
    with open(todosfilepath,'r') as file:
        todos=file.readlines()
    return todos

def save_todos(todosfilepath,todos):
    with open(todosfilepath,'w') as file:
        file.writelines(todos)
        
print("")
todosfilepath = 'todoapp.txt'
todos = get_todos(todosfilepath) # becomes the variable available throughout program

while True :
    print('\nDirectly provide the task along with action')
    useraction = input("add , show, edit, Mark Complete or exit: ").strip()
    if "add" in useraction:
        todo = useraction[4:]
        todos.append(todo+'\n')

        # Open the file and save the variable in the text file
        with open('todoapp.txt','w') as file:
            file.writelines(todos)

    elif useraction == "show" :
        showtodolist(todos)
            # \n will have one space and for loop each element 
            # has built in space while printing each item

    elif useraction == "edit".strip():
        try:
            showtodolist(todos)
            editinput = int(input('Press Number which one to edit :').strip())
            changeditem = input('Enter new item in place :').strip()
            todos[editinput-1] = changeditem+'\n'
            # List is being edited here so we need to open and edit the file again. 
        except ValueError:
            print('Not a valid input')
            pass
    elif useraction == "Complete".strip():
        try:
            showtodolist(todos)
            editinput = int(input('Press Number which one to edit :').strip())
            temp=todos[editinput-1].strip('\n')
            todos.pop(editinput-1) 
            print(f"Item -  {temp} Removed from the list")
        except IndexError:
            print('Not a Valid input')
        except ValueError:
            print('Not a valid input')
            continue
    elif useraction == "exit":
        break
    else :
        print('Choose Correct Action')

save_todos(todosfilepath,todos)        