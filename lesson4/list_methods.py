#Integrated list methods

my_list = ['first', 2]
print(my_list)
#adding element to the end of the list
my_list.append(3)
print(my_list)
#inserting element to list by index
my_list.insert(0, "1")
print(my_list)
#adding several elements to the end of the list
my_list.extend([5, 5, 6])
print(my_list)
my_list.extend('hello')
print(my_list)
#removes first such element from the list
my_list.remove(5)
print(my_list)
#removes all elements from the list
list_for_removing = list(my_list)
list_for_removing.clear()
print(list_for_removing)
#removes element by index (last one if no argument)
my_list.pop(0)
print(my_list)
my_list.pop()
print(my_list)
#returns index of the known element
print(my_list.index('h'))
#returns number of intries of element in the list
print(my_list.count('l'))
#sorts list (modifies list)
second_list = [1, 21,-2, 8, 27, -3, -123]
print(second_list)
second_list.sort()
print(second_list)

# reverses the elements in the list (modifies list)
print(second_list[::-1])
second_list.reverse()
print(second_list)
