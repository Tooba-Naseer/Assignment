"""Python 3.6.7"""
"""File System App"""


import os
import re


def is_found(filename):
    """Returns true if file exists, otherwise returns false.
    """
    
    return os.path.isfile(f"{filename}.txt")

    
def create(filename):
    """Create the file.
    """
    
    with open(f"{filename}.txt","w") as file:
        print("File created successfully!")
    return


def update_append(filename):
    """Update the content of file by appending the data. If the file does not exists then, it
    will first create the file and then append the data in it.
    """
    
    print("Enter text that you want to append:")
    text = input()
    with open(f"{filename}.txt", "a+") as file:
        file.write(text)
    print("File updated successfully!")
    return


def update_overwrite(filename):
    """Update the content of file by overwriting.
    """
    
    print("Enter text:")
    text = input()
    with open(f"{filename}.txt", "w") as write_obj:
        write_obj.seek(0)
        write_obj.write(text)
        write_obj.truncate()
        print("File updated successfully!")
    return


def remove(filename):
    """Remove the file.
    """
    
    os.remove(f"{filename}.txt")
    print("File removed successfully!")
    return


def show_content(filename):
    """Display the content of the file.
    """
    
    with open(f"{filename}.txt","r") as file:
        content = file.read()
        print(content)
    return



def search(filename, string):
    """Search desired string in a file and prints all line numbers and corresponding
       line contents where string founds. If string not founds, then display the
       message.
    """
    
    is_found = False
    with open(f"{filename}.txt", "r") as read_obj:
        for i, item in enumerate(read_obj):
            if string in item:
                print(f"{string} found in line number {i+1} and line contents are:\n{item.rstrip()}")
                is_found = True
                
    if not is_found:
        print(f"{string} Not found!")
    return
   

def replace_word(filename, word, new_word):
    """Replaces the older word with the new word in a file.
    """
    
    with open(f"{filename}.txt", "r+") as read_write_obj:
        text = read_write_obj.read()
        text = re.sub(word, new_word, text)   # replace the given regular expression with new_word
        read_write_obj.seek(0)
        read_write_obj.write(text)
        read_write_obj.truncate()
        print("Word replaced successfully!")
    return


def display():
    """Displays the menu.
    """
    
    print("Choose an option")
    print ("""
    1. Create a file
    2. Update file content (Append)
    3. Update file content (Overwrite)
    4. Remove a file
    5. Show file content
    6. Search a string in a file
    7. Replace a word with other word
    8. Exit
    """)
    return


def main():
    while True:
        display()
        option = input()
        options = [str(i) for i in range(1,9)]

        # check that option is valid or not
        if option not in options:
            print("Invalid option!")
            continue

        # check for exit option
        if option == '8':
            break
        print("Enter file name:")
        filename = input()

        # check that file exists or not and option is in desired options
        if not is_found(filename) and option in options[2:7]:
            print("File not exists!")
            continue
        
        # invoke create function if file not exists already
        if option == '1':
            if is_found(filename):
                print("File exists already!")
                continue
            create(filename)
        elif option == '2':
            update_append(filename)    
        elif option == '3':
            update_overwrite(filename)
        elif option == '4':
            remove(filename)
        elif option == '5':
            show_content(filename)

        # invoke search function after getting string from user   
        elif option == '6':
            print("Enter string for search:")  
            string = input()   
            search(filename, string)

        # invoke replace_word function after getting older and new word from user   
        elif option == '7':
            print("Enter the word that you wants to be replaced:")
            word = input()    
            print("Enter new word:")
            new_word = input()   
            replace_word(filename, word, new_word)
    return


if __name__ == "__main__":
    main()
