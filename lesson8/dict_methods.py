a = {'short': 'dict', 'long': 'dictionary'}

#clear - clears the dictionary
# a.clear()
# print(a)

#copy - copies dictionary 
# b = a.copy()
# print(b)
# b = dict(a)
# print(b)

#get - get value by key. First parameter is key, the second is default value ("None" by default)
# print(a['long'])
# print(a.get('long'))
# print(a.get('longasdasdafsa'))
# print(a.get('longasdasdafsa', "DEFAULT VALUe"))

#pop - deletes item by key, returns value
# var = a.pop("short")
# print(var)
# print(a)

#popitem - deletes last item, returns pair key:value
# var = a.popitem()
# print(var, type(var))

#update - appends pairs key:value to dictionary
b = {'new key': 'new value', 'asd': 'agads2dwa'}
a.update(b)
print(a)

#items() keys() values() - to iterate the dictionary
for item in a.keys():
    print(item)

for item in a.values():
    print(item)

for key, value in a.items():
    print(key, value)