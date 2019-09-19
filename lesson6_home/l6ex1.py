import re

path = input("Please enter path: ")

#C:\Users\Falcon\Documents\python_basic\lesson5_home.asdfasd\1l5ex2.py

class FileNotFoundException(Exception):
    pass

file_name = re.findall(r'\b\w+\.\w+$', path)

if len(file_name) == 0:
    raise FileNotFoundException
else:
    print("File extension is:", re.sub(r'\b\w+\.', '', file_name[0]))

