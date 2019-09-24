import re


def input_phone_number():
    phone_number = input("Enter phone number: ")

    if re.findall(r'[a-zA-Z]', phone_number):
        print("Phone number can't contain letters!")
        return input_phone_number()

    clean_phone_number = re.sub(r'\D', '', phone_number)
    validation = len(clean_phone_number) == 12
    
    if validation:
        return phone_number
    else:
        print("You should enter valid number!")
        return input_phone_number()

def input_password():
    password = input("Enter password: ")
    if len(password) < 8:
        print("Password is too short!")
        return input_password()
    else:
        pass_confirmation = input("Confirm password: ")
        if pass_confirmation == password:
            # print('----------------------------------------')
            # print(password)
            # print(pass_confirmation)
            # print('----------------------------------------')
            return pass_confirmation
        else:
            print("Password and password confirmation don't match!")
            return input_password()



phone_number = input_phone_number()
password = input_password()
# print("The 1 password is:", password)
password = re.sub(r'.', r'*', password)
print("The phone number is:", phone_number)
print("The password is:", password)