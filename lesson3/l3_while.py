# a = 0
# while (a < 10): 
#     print(a)
#     a += 1
########################################################
# a = 0
# while a < 10:
#     if a == 5:
#         print("a ravno 5!")
#         break #прерывает цикл, т.е. в строку 13
#     print(a)
#     a +=1 
######################################################
# a = 0
# while a < 10:
#     if a == 3:
#         print("a = 3!")
#         continue #возвращает в начало цикла, в строку 15
#     if a == 5:
#         print("a ravno 5!")
#         break
#     print(a)
#     a +=1 
#######################################################
while True:
    a = int(input("1st number "))
    b = int(input("2nd number "))

    print(a+b)
    
    answer = input("Continue? yes/no ")
    if answer == "no":
        break
