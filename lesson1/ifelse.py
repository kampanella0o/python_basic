# name = "Da"
# if name == "Max":
#     print(name)    
# else:
#     print('Its not Max')
# a = 10
# b = 15
############################################################
# if a == 10:
#     c = True
# else:
#     if b == 10:
#         c = False
#     else:
#         c = True

# c = True if a == 10 else False if b == 10 else True

# c = True if a == 10 else False
###########################################################
# try:
#     print(10/0)
#     print(a/10)
# except ZeroDivisionError as e:
#     print(e)
#     print("OLOLO")
# except NameError:
#     print("not defined")
# else: #выполняется если не было поймано эксептов
#     print(a)
# finally: #выполняется всегда
#     print('eta finish')
###################################################################
try:
    a = 10
    b = 0
    if b!= 0:
        c = a/ b
    else:
        raise Exception('Devision by zero!')
except Exception as e:
    print(e)
    print("in exception")