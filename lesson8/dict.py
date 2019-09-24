a = {'short': 'dict', 'long': 'dictionary'}
print(a, type(a))
##################################################

b = dict(short='dict', long='dictionary')
print(b, type(b))

print(a['short'])
###############################################################
a['ololo'] = 'lalala' #adding to dictionary (or replacing)
print(a)
print('----------------------------------------')
################################################################
dict_c = {}
dict_c = dict_c.fromkeys(['a', 'b', 'c']) #creates dictionary with iterable object as keys
print(dict_c)
#################################################
dict_d = {i: i ** 2 for i in range(10)} #fills the dictionary with generator
dict_e = {i: i * 2 for i in "abcd"} #fills the dictionary with generator
print(dict_d)
print(dict_e)