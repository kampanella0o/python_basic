def func():
    x = 10
    def summ():
        print(5 + x)
    return summ

var = func()

print(var, type(var))