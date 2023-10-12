# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:01:45 2023

@author: pandey
List of All Functions that are supporing the To Do App

"""
FILEPATH="todoapp.txt"
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
    
def get_todos(todosfilepath=FILEPATH):
    
    todos = []  #todos must be a list 
    with open(todosfilepath,'r') as file:
        todos=file.readlines()
    return todos

def save_todos(todos,todosfilepath=FILEPATH):
    with open(todosfilepath,'w') as file:
        file.writelines(todos)