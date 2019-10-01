from classes import User

class Admin(User):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.__company = company

    def display_info(self):
        print(f'{self.name}, age: {self.age}\nCompany: {self.__company}')

admin1 = Admin('Admin', 33, 'Google')
user1 = User('Uasya', 24)
admin1.display_info()
user1.display_info()