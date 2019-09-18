#For example, we want to display string output left justified or in the center or we want to show the number in the various formats.
#n = 2 

import re

sentence = input("Please enter sentence: ")
n = int(input("Please enter number of repetitions to delete: "))

words = re.sub(r"\W |\W$", ' ', sentence)
words = words.split()
result_sentence = sentence

for w in words:
    list_of_repetitions = re.findall(r'\b' + w + r'\b', result_sentence)
    if len(list_of_repetitions) == n:
        result_sentence = re.sub(r'\b' + w + r'\b', '', result_sentence)

result_sentence = re.sub(r'\s+', ' ', result_sentence)

print(result_sentence)