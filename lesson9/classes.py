class Person:
    
    def __init__(self, name, age='18', city="London"):
        self.name = name
        self.age = age
        self.city = city

    def print_name(self):
        print(self.name)

    def change_name(self, new_name):
        self.name = new_name

obj = Person('Maks')
obj2 = Person('Kurka')

obj.name = "Max"
# print(obj.name)
# print(obj2.name)

obj.print_name()
obj.change_name('Ololo')
obj.print_name()
