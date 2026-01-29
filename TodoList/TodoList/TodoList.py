toDoList = []
def menu():
    while True:
        print("Todo List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("What would you like to do? ")
        match choice:
            case "1":
                view_task()
            case "2":
                add_task()
            case "3":
                remove_task()
            case "4":
                print("Goodbye!")    
                break
            case _:
                print("Invalid input, try again")

def view_task():
    if toDoList == []:
        print("You currently have no tasks to view, add some next time!")
    else:
        print(toDoList)
    
                        
def add_task():
    task = input("What task would you like to add? ").capitalize()
    toDoList.append(task)
    print(f'Task "{task}" added to the list.')

def remove_task():
    if toDoList == []:
        print("You have no tasks that can be removed, add some next time!")
    else:
        task = input("What task would you like to remove?").capitalize()
        toDoList.remove(task)
        print(f'You have successfully removed "{task}" from the list.')    

menu()


