# a = ['1', '2', '3', '4', '5']

# #copying
# b = list(a)
# c = a[:]

# #making a link
# d = a

# print(a, id(a))
# print(b, id(b))
# print(c, id(c))
# print('*'*20)

# first_list = ['a', 'b', 'c']
# second_list = ['e', 'f', 'g']
# print(first_list+second_list) # elements are added
# print(first_list*2) #elements are shown twice

# first, second, third = ['e', 'f', 'g'] #unpacking elements of the list to the variables
# print(first, second, third)
#####################################################################
#python integrated functions

# numbers = [1, 6, 5, 4, 7, 9, 2, 8, 3]
# words = ['hello', 'ololo', 'a', 'ho']
# print('min', min(numbers)) #minimal value
# print('max', max(numbers)) #maximal value
# print(min(words))
# print(max(words))

# numbers = [1, 6, 5, 4, 7, 9, 2, 8, 3]
# words = ['hello', 'ololo', 'a', 'ho']
# print(sorted(numbers)) #sort from min to max
# print(sorted(words))
# print(numbers)
# print(words)

# a = 10
# del a #deletes object from memory
# print(a)
# numbers = [1, 6, 5, 4, 7, 9, 2, 8, 3]
# print(numbers)
# del numbers[0]
# print(numbers)

numbers = [1, 6, 5, 4, 7, 9, 2, 8, 3]
len(numbers) # returns lenght of the list
print(len(numbers))
print(len("hello!"))