# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:59:32 2023

@author: pandey
# When importing any module it executes it 
# we can have one separte file with all functions 
# Utilizing the if      __name == '__main__' this code block is TRUE 
# only when it is executed fro the same program, if we importa  python
# function from antother file this block is False hence not executed.
# include Time also to note what time to do 

"""
from todoapp_functions import get_todos, save_todos, showtodolist
import time

now = time.strftime("%m-%d-%Y, %H:%M:%S")
print("it is - ",now)
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