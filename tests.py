# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:39:45 2023

@author: pandey

File for testing functionality 
Rough file for test

"""

fnames = ['1.files','2.presentation','3.technicaldocs']

# Transform the list replace . with -
# add .txt extension
# output and input both are list 

fnames = [item.replace('.','-')+'.txt' for item in fnames]
print(fnames)


names = ["john smith", "jay santi", "eva kuki"]
newnames = [item.title() for item in names]
print(newnames)


usernames = ["john 1990", "alberta1970", "magnola2000"]
new = [len(item) for item in usernames]
print(new)

user_entries = ['10', '19.1', '20']
print(sum([float(item) for item in user_entries]))

# save these in a file
temperatures = [10, 12, 14]
file = open("test_files/file.txt", 'w')
file.writelines([str(each)+'\n' for each in temperatures])
file.close()

# return integers 
numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)

#Cursor approach in reading
with open('test_files/file.txt','r') as f:
    print(f.read())
    print(f.read())
    print("")
    print("Notice cursor reached end after first read")

# check how write works
with open('test_files/file.txt','r') as f:
    print(f.read())

with open('test_files/file.txt','w') as f:
    print(f.write('Hellow'))
    
with open('test_files/file.txt','w') as f:
    print(f.write('World'))

with open('test_files/file.txt','r') as f:
    print(f.read())
    
    
# chek how split works


print('hey=how=are=you'.split('='))
# return a list 

