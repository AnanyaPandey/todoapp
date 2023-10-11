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

import time
print(time.strftime('%Y'))
print(time.strftime("%m-%d-%Y, %H:%M:%S"))

import todoapp_functions
dir(todoapp_functions)

# ==== list of useful modules
import glob
# provide what files u want to filter
# glob function returns a list 
myfiles = glob.glob('test_files/*.txt')
print(myfiles)
for each_filepaths in myfiles:
    with open(each_filepaths,'r') as file:
        print(file.read())
        
# Returns all the txt files as a list in current directory

import csv
with open('test_files/filename.csv','r') as file :
    data = list(csv.reader(file))
print(data)

userinput = input("Enter a City: ")
for row in data[1:]: # Exclude the Headers
    if row[0] == userinput : # Match if the input city is present in the data
        print(row[1]) # Print the rows first index column i.e. temprature

# Create search something in browser
import webbrowser
user_ter=input('enter a search')
webbrowser.open('https://www.google.com/search?q='+user_ter)

# Reading from JSON
# note that the file we have in JSON its a list of dictionaries
# Once we have the file we can rred it
import json
with open('test_files/Questions.json','r') as file :
    content = file.read()

print(content)
# Json Load String 

score=0
data = json.loads(content)

# We are iterating over a list.
# if it was dictionary of dictionaries our iteration should be different

for each_Question in data:
    print(each_Question["Question"])
    for index, each_alternative in enumerate(each_Question["Alternatives"]):
        print(index+1," - ", each_alternative)
    
    userchoice = int(input("Enter Your Answe "))
    each_Question["User Choice"] = userchoice
    # adding this to userchoice was imp to compare 
    # because each question as diffrent input
    if each_Question["User Choice"] == each_Question["Answer"]:
        score=score+1
        print("Correct Choice:",each_Question["Answer"])
    else:
        print('Ohh Incorrect, Correct Answer is ',each_Question["Answer"])

print('Your Score: ',score)








