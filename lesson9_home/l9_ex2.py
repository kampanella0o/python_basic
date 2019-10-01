import random

class Customer:

    def __init__(self, first_name, last_name, city=None, tel_number=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.tel_number = tel_number
        self.email = email

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name
        
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_tel_number(self, tel_number):
        self.tel_number = tel_number

    def get_tel_number(self):
        return self.tel_number

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def print_all_info(self):
        pattern = '''
        Customer info
        First name: {}
        Last name {}
        City: {}
        Telephone number: {}
        Email: {}
        '''
        print(pattern.format(self.first_name, self.last_name, self.city, self.tel_number, self.email))

    def __str__(self):
        pattern = '''Customer info
        First name: {}
        Last name: {}
        City: {}
        Telephone number: {}
        Email: {}'''
        return pattern.format(self.first_name, self.last_name, self.city, self.tel_number, self.email)

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

for i in range (0, 15):
    customers.append(Customer(random.choice(first_names), random.choice(last_names), random.choice(cities)))
    customers[i].set_tel_number(generate_phone_number())
    customers[i].set_email("%s_%s%s@gmail.com" % (
        customers[i].get_first_name(), 
        customers[i].get_last_name(), 
        random.randrange(1965, 1999))
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
    operator_code = i.get_tel_number()[0: 3]
    lifecell_codes = ['073', '093', '063']
    if operator_code in lifecell_codes:
        print(i)