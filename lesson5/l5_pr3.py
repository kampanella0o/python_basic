string = input("Please, enter string: ")

if len(string) > 10:
    string = string[0:6]
else:
    while len(string) != 12:
        string = string + "o"

print(string)
