"""Python 3.6.7"""
"""To do list assignment"""

# It is a dictionary that stores all tasks
tasks = {}
Id = 0

def create():
    global Id
    print("Enter the title:")
    title = input()
    print("Enter description:")
    desc = input()
    Id += 1
    tasks[str(Id)] = [title, desc]
    print("Task created successfully!\n")
    return

def get():
    print("Enter id of task you want to get:")
    idd = input()
    if idd not in tasks:
        print("Task id is not present!")
        return
    print("Task Title: "+ tasks[idd][0])
    print("Task Description: " + tasks[idd][1] + "\n")
    return

def update():
    print("Enter id of task you want to update:")
    idd = input()
    if idd not in tasks:
        print("Task id is not present!\n")
        return
    print("Enter the title:")
    title = input()
    print("Enter description:")
    desc = input()
    tasks[idd] = [title, desc]
    print("Task updated successfully!\n")
    return

def delete():
    print("Enter id of task you want to delete:")
    idd = input()
    if idd not in tasks:
        print("Task id is not present!\n")
        return
    del tasks[idd]
    print("Task deleted successfully!\n")
    return
    


def print_data():
    print("{:<10} {:<20} {:<10}".format('Task Id','Title','Description'))
    for key in tasks:
        print("{:<10} {:<20} {:<10}".format(key, tasks[key][0], tasks[key][1]))
    return

def display():
    print("Choose an option")
    print ("""
    1. Create a task
    2. Get a task
    3. Update a task
    4. Delete a task
    5. View all tasks
    6. Exit
    """)
    return

def main():
    while True:
        display()
        option = input()
        if option == '6':
            break
        if option == '1':
            create()
        elif option == '2':
            get()
        elif option == '3':
            update()
        elif option == '4':
            delete()
        elif option == '5':
            print_data()
        else:
            print("Invalid option!\n")
    return

if __name__ == "__main__":
    main()
