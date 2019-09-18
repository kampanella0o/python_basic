import re

path = input("Please enter path: ")

#C:\Users\Falcon\Documents\python_basic\lesson5_home.asdfasd\1l5ex2.py

file_name = re.findall(r'\b\w+\.\w+$', path)
print("File name is:", re.sub(r'\.\w+$', '', file_name[0]))