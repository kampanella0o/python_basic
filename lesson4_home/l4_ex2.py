n = '0'

while int(n) <= 0:
    n = input("Please enter a natural number: ")
    try:
        int(n)
    except ValueError:
        print("You should enter a natural number!")
        n = '0'

number_of_digits = len(n)

if number_of_digits == 1:
    summ_of_digits = n
else:
    while number_of_digits != 1:
        summ_of_digits = 0
        for digit in n:
            summ_of_digits += int(digit)
        n = str(summ_of_digits)
        number_of_digits = len(str(summ_of_digits))
        
print(summ_of_digits)
