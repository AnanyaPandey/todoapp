
# to do app version 1.3
# Numbered to dos.
# enumerate(List) -> returns item and index both
# use of F-strings
# f"Use text along with {expresion} anyhting within {} is evaluated"
# file.read reads everything in single string single object readlines consider each object as diff line
# Same with write and writelines.
# ONCE a file is read the reader reaches at the end of file so next time if we read the file without opening it 
# it will return ''

print("")
todos = []
file=open('todoapp.txt','r')
todos=file.readlines()
file.close()

while True :
    useraction = input("add , show, edit, Mark Complete or exit: ").strip()
    if useraction == "add":
        todo =input("enter a todo item: ") + '\n'
        todos.append(todo)

        # Open the file and save the variable in the text file
        file = open('todoapp.txt','w')
        file.writelines(todos)
        file.close()

    elif useraction == "show" :
        for i,item in enumerate(todos):
            print(f"{i+1}-{item}")
            # \n will have one space and for loop each element 
            # has built in space while printing each item

    elif useraction == "edit".strip():
        for i,item in enumerate(todos):
            print(f"{i}-{item}")
        editinput = int(input('Press Number which one to edit :').strip())
        changeditem = input('Enter new item in place :').strip()
        todos[editinput-1] = changeditem

        # List is being edited here so we need to open and edit the file again. 

    elif useraction == "Complete".strip():
        for i,item in enumerate(todos):
            print(f"{i+1}-{item}")
        editinput = int(input('Press Number which one to edit :').strip())
        todos.pop(editinput-1) 
    elif useraction == "exit":
        break
    else :
        print('Choose Correct Action')
