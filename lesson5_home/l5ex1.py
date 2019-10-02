import re

def input_numbers():
    numbers = input("Enter numbers in format '1 + 1 - 1 + 1' ('+' and '-' can be used): ")
    validation = re.match(r'(\d+ [+-] ){3}\d+', numbers)
    if validation:
        print(validation)
        return numbers
    else:
        print("You should use proper format!")
        return input_numbers()



# numbers = input_numbers()
# list_of_strings = numbers.split()

# for i in range(1, len(list_of_strings), 2):
#     if list_of_strings[i] == "-":
#         list_of_strings[i+1] = - int(list_of_strings[i+1])

# result = 0

# for i in range(0, len(list_of_strings), 2):
#     result += int(list_of_strings[i])

numbers = input_numbers()
numbers = numbers.split('+')
result = 0

for i in numbers:
    minus = i.split('-')
    if len(minus) > 1:
        result += int(minus[0]) - sum(map(int, minus[1:]))
    else:
        result += int(i)


print("Result is:", result)
