
# to do app version 1.2
todos = []

while True :
    useraction = input("add , show, edit or exit: ").strip()
    if useraction == "add":
        todo =input("enter a todo item: ").strip()
        todos.append(todo)
    elif useraction == "show" :
        for i in range(0,len(todos)):
            print(i+1,"-",todos[i])
    elif useraction == "edit".strip():
        for i in range(0,len(todos)):
            print(i+1,"-",todos[i])
        editinput = int(input('Press Number which one to edit :').strip())
        changeditem = input('Enter new item in place :').strip()
        todos[editinput-1] = changeditem
    elif useraction == "exit":
        break
    else :
        print('Choose Correct Action')