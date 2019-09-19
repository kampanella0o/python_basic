import os

with open("sample_text", 'r') as original_text:
    string = original_text.read()

lines = string.split('\n')

try:
    os.mkdir("ex1 result")
except FileExistsError:
    pass

with open("ex1 result\\result_text", 'w') as new_text:
    for line in lines:
        new_line = line.split()
        new_line.reverse()
        for word in new_line:
            new_text.write(word + ' ')
        new_text.write('\n')

