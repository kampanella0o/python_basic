string = input("Please, enter string: ")

if string[0:3] == "abc":
    new_string = "www" + string[3:]
else:
    new_string = string + "zzz"

print(new_string)
