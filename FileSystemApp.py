"""Python 3.6.7"""
"""File System App"""

import os
import re


def is_found(filename):
    """Returns true if file exists, otherwise returns false.
    """
    
    if os.path.isfile(f"{filename}.txt"):
        return True
    return False
    
def create(filename):
    """If the file does not exist then create the file
       otherwise display the message that file exists.
    """
    
    if is_found(filename):
        print("File exists already!")
        return
    file = open(f"{filename}.txt","w")
    file.close()
    print("File created successfully!")
    return

def remove(filename):
    """If file exists then remove the file otherwise
       display the message that file does not exists.
    """
    
    if not is_found(filename):
        print("File not exists!")
        return
    os.remove(f"{filename}.txt")
    print("File removed successfully!")
    return

def show_content(filename):
    """If file exists then display the content of file.
    """
    
    if not is_found(filename):
        print("File not exists!")
        return
    file = open(f"{filename}.txt","r")
    content = file.read()
    print(content)
    file.close()
    return

def update_append(filename):
    """Update the content of file by appending the data. If the file does not exists then, it
    will first create the file and then append the data in it.
    """
    
    print("Enter text that you want to append:")
    text = input()
    file = open(f"{filename}.txt", "a+")
    file.write(text)
    file.close()
    print("File updated successfully!")
    return

def update_overwrite(filename):
    """Update the content of file by overwriting.
    """
    
    if not is_found(filename):
        print("File not exists!")
        return
    print("Enter text:")
    text = input()
    with open(f"{filename}.txt", "w") as write_obj:
        write_obj.seek(0)
        write_obj.write(text)
        write_obj.truncate()
        write_obj.close()
        print("File updated successfully!")
    return

def search(filename, string):
    """Search desired string in a file and prints all line numbers and corresponding
       line contents where string founds. If string not founds, then display the
       message.
    """
    
    if not is_found(filename):
        print("File not exists!")
        return
    flag = 0
    with open(f"{filename}.txt", "r") as read_obj:
        for item in enumerate(read_obj):
            if string in item[1]:
                print(f"{string} found in line number {item[0]+1} and line contents are:\n{item[1].rstrip()}")
                flag = 1
        read_obj.close()
    if flag == 0:
        print(f"{string} Not found!")
    return
   

def replace_word(filename, word, new_word):
    """Replaces the older word with the new word in a file.
    """
    
    if not is_found(filename):
        print("File not exists!")
        return
    with open(f"{filename}.txt", "r+") as read_write_obj:
        text = read_write_obj.read()
        # replace the selected regular expression with new word
        text = re.sub(word, new_word, text) 
        read_write_obj.seek(0)
        read_write_obj.write(text)
        read_write_obj.truncate()
        read_write_obj.close()
        print("Word replaced successfully!")
    return

def display():
    print("Choose an option")
    print ("""
    1. Create a file
    2. Remove a file
    3. Show file content
    4. Update file content (Append)
    5. Update file content (Overwrite)
    6. Search a string in a file
    7. Replace a word with other word
    8. Exit
    """)
    return

def main():
    while True:
        display()
        option = input()
        options = map(lambda x: str(x), list(range(1,9)))
        if option not in options:
            print("Invalid option!")
            continue
        if option == '8':
            break
        print("Enter file name:")
        filename = input()
        if option == '1':
            create(filename)
        elif option == '2':
            remove(filename)
        elif option == '3':
            show_content(filename)
        elif option == '4':
            update_append(filename)
        elif option == '5':
            update_overwrite(filename)
        elif option == '6':
            print("Enter string for search:")
            string = input()
            search(filename, string)
        elif option == '7':
            print("Enter the word that you wants to be replaced:")
            word = input()
            print("Enter new word:")
            new_word = input()
            replace_word(filename, word, new_word)
    return

if __name__ == "__main__":
    main()
