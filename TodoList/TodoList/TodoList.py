toDoList = []
def add_task(task):
    toDoList.append(task)
    print(f'Task "{task}" added to the list.')
add_task(input("Enter a task to add: "))   