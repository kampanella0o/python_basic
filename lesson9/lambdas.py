# func lambda x,y: x*y

# def func(x,y):
#     return x*y

#^^^^ same result for both


# func = lambda x,y: x + y

# result = func(1, None)

# print(result)

a = [1, 2, 3, 4, 5, 6]
b = [2, 2, 2, 2, 3, 3]

# result = list(map(str, a))
result = list(map(lambda x: x*2, a))
result1 = [x*2 for x in a]
print(result1)
print(result)

result = list(map(lambda x, y: x**y, a, b))
print(result)

result2 = filter(lambda x: x <5, a)
print(list(result2))