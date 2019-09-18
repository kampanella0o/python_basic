import os

# print(os.getcwd()) #shows current dir
# print(os.listdir("../../")) #list that contains all files in folder
# os.rename("file to rename.txt", "file to rename1.txt") #renames file
# os.mkdir("DIR!") #creates directory (can't be nested)
# os.makedirs('path/to/dir') #creates directory - can be nested
# os.rmdir("DIR!") #removes directory (only empty one)
# os.remove("DIR!") #removes non-empty dir (should be owner to delete dir) or file

os.system("echo chromedriver.exe") #system commands can be used

from os.path import isfile

for i in os.listdir('.'):
    if isfile(i): #returns true if its file
        print("File")
    else:
        print("Folder")

import sys


sys.path.append(r"C:\Users\Falcon\Documents\python_basic\lesson1") #adds 