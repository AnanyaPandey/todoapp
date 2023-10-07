# userpromt = 'enter your todo'
# todos = []
# while todo != 0:
#     todo=input(userpromt)
#     todos.append(todo)
# print(todos)



# password check
password = input('Enter a password')
def passcheck(password):
    while password != 'Pass123':
        print('Wrong Password Try Again!')
        password = input('enter a password: ')
    print('Correct!')
    return 

# Passpasscheck(password)

def checkcountry():
    countries = []
 
    while len(countries) <6:
        country = input("Enter the country: ")
        countries.append(country)
    print(countries)

checkcountry()

# How To Find What you need ????
# use Python Console

dir(str)

# __method__ are used python internally
# at the end alphabetally methods are listed.

# help(str.method)
help(str.capitalize) # Tells what the method does.

dir(list)
list1 = [1,2,3,4,5]
dir(list1) # also works 

help(list1.append)

# check if the merhods has argument or not if it has argument it takes argument otherwise datatype.method()
# ========================

# To get the built in functions 

import builtins
dir(builtins)




