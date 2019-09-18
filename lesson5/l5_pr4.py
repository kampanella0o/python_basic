def input_number_of_strings():
    number_of_strings = input("Enter number of strings: ")
    try:
        if '.' not in number_of_strings != int and int(number_of_strings) > 0:
            return int(number_of_strings)
        else:
            print("You should enter valid number!")
            input_number_of_strings()
    except ValueError:
        print("You should enter valid number!")
        input_number_of_strings()

number_of_strings = input_number_of_strings()
result_string = ''

for i in range(0, number_of_strings):
    result_string += input("Please enter string " + str(i + 1) + ": " )

print("Result is", result_string)