file_name = open("C:\\Users\\Falcon\\Documents\\python_basic\\lesson7\\file.txt", 'r')
# print(file_name.read(5)) #reads first 5 bytes
# print(file_name.tell()) #returns current coursor index
# file_name.seek(0) #moves coursor 
# print(file_name.tell())
# print(file_name.read(5))


# for line in file_name:
#     print(line) #prints file by lines

# print(file_name.readline()) #returns file by lines
# print(file_name.readline())

print(file_name.readlines()) #makes list of lines of file

file_name.close()

file_name = open("C:\\Users\\Falcon\\Documents\\python_basic\\lesson7\\file.txt", 'w') #deletes old file and creates new one (creates new if file doesn't exist)
file_name.write("Some string")
print("some values", file=file_name)
file_name.close()

# file1 = open("text.txt", 'r')
# try:
#     file1.write()
# except:
#     print()
# finally:
#     file1.close()

with open("C:\\Users\\Falcon\\Documents\\python_basic\\lesson7\\file.txt", 'a') as file_name:
    print(file_name.write("new text"))