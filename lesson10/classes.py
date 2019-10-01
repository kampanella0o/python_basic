class User:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property #getter
    def age(self):
        return self.__age

    @property #getter
    def name(self):
        return self.__name

    @age.setter #setter
    def age(self, age):
        if age in range(1, 100):
                self.__age = age
        else:
            print("Invalid age")
    
    def display_info(self):
        print(f'{self.__name}, age: {self.__age}')

    # def __del__(self):
    #     print(self.__name, 'removed')

    def __str__(self):
        return self.__name


user = User('Jack', 25)

print(user.__dict__)
# user.display_info()

# user.set_age(2)
# user.age #get via getter

# user.age = 25 #set via setter
# user.age