"""Python 3.6.7"""
"""To do list assignment"""


class Task:
    
    counter = 0
    
    # Intializing
    def __init__(self, title, description):
        Task.counter += 1
        self.Id = Task.counter
        self.title = title
        self.description = description

    # Get task
    def get(self):
        print(f"Task Title: {self.title}")
        print(f"Task Description: {self.description}")
        return

    # Update task
    def update(self, title, description):
        self.title = title
        self.description = description
        return

    # Print task object
    def __str__(self):
        return "{:<10} {:<20} {:<10}".format(self.Id, self.title, self.description)



def print_data(tasks):
    """Print all tasks in a table like format.
    """
    
    print("{:<10} {:<20} {:<10}".format('Task Id','Title','Description'))
    for task in tasks:
        print(task)
    print("\n")
    return


def get_position(Id, tasks):
    """Returns the desired task's position. If the task does not found,
       then display task not found message and return None.
    """
    
    for i, item in enumerate(tasks):
        if Id == str(item.Id):
            return i
    print("Task id is not found!")
    return None     


def display():
    """Displays the menu.
    """
    
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


def ask():
    """Ask the user to enter the title and description of a task. It will then return what user entered.
    """
    
    print("Enter the title:")
    title = input()
    print("Enter description:")
    description = input()
    return title, description


def main():
    tasks = []    # It contains objects of Task class
    while True:
        display()
        option = input()

        # Check for exit option
        if option == '6':
            break

        # This option creates the task
        if option == '1':
            title, description = ask()
            task = Task(title, description)
            tasks.append(task)
            print("Task created successfully!\n")

        # If the task exists, then this option will fetch the task   
        elif option == '2':
            print("Enter id of task you want to get:")
            Id = input()
            i = get_position(Id, tasks)
            if i is not None:
              tasks[i].get()

        # If the task exists, then this option will update the task     
        elif option == '3':
            print("Enter id of task you want to update:")
            Id = input()
            i = get_position(Id, tasks)
            if i is not None:
              title, description = ask()
              tasks[i].update(title, description)
              print("Task updated successfully!\n")

        # If the task exists, then this option will delete the task     
        elif option == '4':
            print("Enter id of task you want to delete:")
            Id = input()
            i = get_position(Id, tasks)
            if i is not None:
              del tasks[i]
              print("Task deleted successfully!\n")

        # This option displays all the tasks     
        elif option == '5':
            print_data(tasks)

        # Invalid option  
        else:
            print("Invalid option!\n")
    return


if __name__ == "__main__":
    main()
