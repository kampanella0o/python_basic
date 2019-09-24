import re

text = 'some text the text here some text i like this text'

result = {}

for char in text:
    result[char] = len(re.findall(char, text))

# for char in text:
#     try:
#         result[char] += 1
#     except:
#         result[char] = 1

print(result)