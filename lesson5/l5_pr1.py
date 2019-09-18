string = input("Please, enter string: ")

if len(string) > 5:
    new_string = string[0:3].upper() + string[3:]
    new_string = new_string[:-3] + new_string[-3:].lower()
    print(new_string)
else:
    for i in string:
        print(string[0].swapcase())
