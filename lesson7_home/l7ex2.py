import os
import re


with open("sample_list", encoding = 'utf-8', mode = 'r') as original_text:
    string = original_text.read()

lines = string.split('\n')

try:
    os.mkdir("ex2 result")
except FileExistsError:
    pass

with open("ex2 result\\result_list", encoding = 'utf-8', mode = 'w') as new_text:
    for line in lines:
        temp_line = line.lower()
        temp_line = temp_line.lstrip()
        temp_line = temp_line.rstrip()
        if temp_line.startswith("а") or temp_line.startswith("м"):
            temp_line = re.sub(r'\D', '', temp_line)
            new_text.write(temp_line + '\n')