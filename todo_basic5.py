# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:31:37 2023

@author: pandey

# Introduce - List Comprehension
# Reduce the extra space in show 
# When youwant to do something where input is list and output is list
# There u can use list comprehension
# introduce the context manager "WITH"
# with context manager closes the file automatically

"""

print("")
todos = []  #todos must be a list 
with open('todoapp.txt','r') as file:
    todos=file.readlines()

while True :
    useraction = input("add , show, edit, Mark Complete or exit: ").strip()
    if useraction == "add":
        todo =input("enter a todo item: ") + '\n'
        todos.append(todo)

        # Open the file and save the variable in the text file
        with open('todoapp.txt','w') as file:
            file.writelines(todos)

    elif useraction == "show" :
        newtodos = [item.strip('\n') for item in todos]
        for i,item in enumerate(newtodos):
            print(f"{i+1}-{item}")
            # \n will have one space and for loop each element 
            # has built in space while printing each item

    elif useraction == "edit".strip():
        for i,item in enumerate(todos):
            print(f"{i+1}-{item}")
        editinput = int(input('Press Number which one to edit :').strip())
        changeditem = input('Enter new item in place :').strip()
        todos[editinput-1] = changeditem+'\n'
        # List is being edited here so we need to open and edit the file again. 

    elif useraction == "Complete".strip():
        for i,item in enumerate(todos):
            print(f"{i+1}-{item}")
        editinput = int(input('Press Number which one to edit :').strip())
        temp=todos[editinput-1].strip('\n')
        todos.pop(editinput-1) 
        print(f"Item -  {temp} Removed from the list")
        
    elif useraction == "exit":
        break
    else :
        print('Choose Correct Action')

with open('todoapp.txt','w') as file:
    file.writelines(todos)