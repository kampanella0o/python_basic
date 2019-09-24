def add(*args):
    print(sum(args))

my_list = [1, 2, 3]

add(5, 8, 10)
add(*my_list)


def printilda(**kwargs):
    print(kwargs)

printilda(name='ololo', afiu='fibas')