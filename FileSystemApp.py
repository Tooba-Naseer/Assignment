"""Python 3.6.7"""
"""File System App"""

import os
import re

def create(filename):
    """Create the file if file already not exists
       otherwise print file existed message.
    """
    
    if os.path.isfile(filename+".txt"):
        print("File existed already!")
        return
    file = open(filename + ".txt","w")
    file.close()
    print("File created successfully!")
    return

def remove(filename):
    """Remove the file if file exists otherwise
       print file not existed message.
    """
    
    if not os.path.isfile(filename+".txt"):
        print("File not exist!")
        return
    os.remove(filename + ".txt")
    print("File removed successfully!")
    return

def show_content(filename):
    """Display the content of file if file exists.
    """
    
    if not os.path.isfile(filename+".txt"):
        print("File not exist!")
        return
    file = open(filename + ".txt","r")
    content = file.read()
    print(content)
    file.close()
    return

def update_append(filename):
    """Update the content of file by appending, if file not exist then, it
    will first create the file and then append data in it.
    """
    
    print("Enter text that you want to append:")
    txt = input()
    file=open(filename + ".txt", "a+")
    file.write(txt)
    file.close()
    print("File updated successfully!")
    return

def update_overwrite(filename):
    """Update the content of file by overwriting.
    """
    
    if not os.path.isfile(filename+".txt"):
        print("File not exist!")
        return
    print("Enter text:")
    txt = input()
    with open(filename + ".txt", "r+") as readWriteObj:
        text = readWriteObj.read()
        text = re.sub(text[0:len(txt)], txt, text)
        readWriteObj.seek(0)
        readWriteObj.write(text)
        readWriteObj.truncate()
        readWriteObj.close()
        print("File updated successfully!")
    return

def search(filename,string):
    """Search desired string in file and prints all line numbers and corresponding
       line contents where string founds. If string not founds, then display the
       message.
    """
    
    if not os.path.isfile(filename+".txt"):
        print("File not exist!")
        return
    lineNo = 0
    lines=[]
    with open(filename + ".txt", "r") as readObj:
        for line in readObj:
            lineNo += 1
            if string in line:
                lines.append((lineNo, line.rstrip()))
        readObj.close()
    if len(lines) == 0:
        print(string + " Not found!")
        return
    for each in lines:
        print(string + " found in line number " + str(each[0]) + " and line contents are:\n" + each[1])
    return

def replace_word(filename, word, newWord):
    """Replace older word with new word in a file.
    """
    
    if not os.path.isfile(filename+".txt"):
        print("File not exist!")
        return
    with open(filename + ".txt", "r+") as readWriteObj:
        text = readWriteObj.read()
        # replace the selected regular expression with new word
        text = re.sub(word, newWord, text) 
        readWriteObj.seek(0)
        readWriteObj.write(text)
        readWriteObj.truncate()
        readWriteObj.close()
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
        if option not in ('1','2','3','4','5','6','7','8'):
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
            search(filename,string)
        elif option == '7':
            print("Enter word to be replaced:")
            word = input()
            print("Enter new word:")
            newWord = input()
            replace_word(filename, word, newWord)
    return

if __name__ == "__main__":
    main()
