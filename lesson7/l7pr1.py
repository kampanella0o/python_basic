
file = open('l7pr1.txt', 'w')

for i in range (9, 18):
    # file.write(str(i) + " ")
    print(i, file=file, end=' ')

file.close()

with open("l7pr1.txt", 'a') as file:
    file.write('\nOlolO )86@#!&@^(8274)')

import re

def get_upper(string_to_check):
    result = re.findall(r'[A-Z]', string_to_check)
    return len(result)

def get_lower(string_to_check):
    result = re.findall(r'[a-z]', string_to_check)
    return len(result)

def get_numbers(string_to_check):
    result = re.findall(r'\d', string_to_check)
    return len(result)

def get_special_symbols(string_to_check):
    # result = re.findall(r'\W\S', string_to_check)
    re.sub(r'\s', '', string_to_check) #replaces something that matches the pattern to new string and saves to variable
    result = re.findall(r'\W', string_to_check)
    return len(result)

with open("l7pr1.txt") as file:
    data = file.read()

print(get_upper(data))
print(get_lower(data))
print(get_numbers(data))
print(get_special_symbols(data))

# '[A-Z]', '[a-z]', ''
