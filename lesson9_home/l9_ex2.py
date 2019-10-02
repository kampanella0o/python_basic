import random

class Customer:

    def __init__(self, first_name, last_name, city=None, tel_number=None, email=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__city = city
        self.__tel_number = tel_number
        self.__email = email
    
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    
    @property
    def city(self):
        return self.__city

    @city.setter
    def set_city(self, city):
        self.__city = city

    @property
    def tel_number(self):
        return self.__tel_number

    @tel_number.setter
    def tel_number(self, tel_number):
        self.__tel_number = tel_number

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email



    def print_all_info(self):
        pattern = '''
        Customer info
        First name: {}
        Last name {}
        City: {}
        Telephone number: {}
        Email: {}
        '''
        print(pattern.format(self.__first_name, self.__last_name, self.__city, self.__tel_number, self.__email))

    def __str__(self):
        pattern = '''Customer info
        First name: {}
        Last name: {}
        City: {}
        Telephone number: {}
        Email: {}'''
        return pattern.format(self.__first_name, self.__last_name, self.__city, self.__tel_number, self.__email)

first_names = ['Vasya', 'Kolya', 'Vanya', 'Dima', 'Olga', 'Liuba', 'Katya', 'Maryna']
last_names = ['Petrov', 'Sidorov', 'Vetrenko', 'Gridorenko', 'Abc', 'Bochkarev', 'Fedorov']
cities = ['Kyiv', 'Kharkriv', 'Jytomyr', 'Rivne', 'Lviv']

def generate_phone_number():
    operator_codes = ['067', '097', '050', '095', '073', '093', '063']
    number = ''
    for i in range (0, 7):
       number = number + str(random.randrange(0, 10))
    return random.choice(operator_codes) + number

customers = []

sadsad = Customer('asd', 'asdasfa')

for i in range (0, 15):
    customers.append(Customer(random.choice(first_names), random.choice(last_names), random.choice(cities)))
    customers[i].tel_number = generate_phone_number()
    customers[i].email = "%s_%s%s@gmail.com" % (
        customers[i].first_name, 
        customers[i].last_name,
        random.randrange(1965, 1999)
        )


# for i in customers:
#     print(i)
# print('-------------------------------------------')

print(customers[0])
print(customers[1])
print(customers[2])
print('-------------------------------------------')

customers.sort(key=lambda customer: customer.last_name)

print(customers[0])
print(customers[1])
print(customers[2])

print("\n\n-----------------------------------\nCustomers, which use lifecell:")
for i in customers:
    operator_code = i.tel_number[0: 3]
    lifecell_codes = ['073', '093', '063']
    if operator_code in lifecell_codes:
        print(i)