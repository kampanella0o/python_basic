import re

def input_phone_number():
    phone_number = input("Enter phone number like '+9(999)99-99-999': ")
    validation = re.match(r'\+\d\d\(\d{3}\)\d\d\-\d\d\-\d{3}', phone_number)
    
    if validation:
        return phone_number
    else:
        print("You should enter valid number!")
        input_phone_number()


phone_number = re.sub(r'\D', '', input_phone_number())
print(phone_number)