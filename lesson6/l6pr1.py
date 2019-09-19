import random

some_array = [1, 2, 15, 34, 5, -1, 8]

def some_func(array):
    shuffled_array = array
    random.shuffle(shuffled_array)
    print(shuffled_array)
    mult = 1
    for i in shuffled_array:
        if shuffled_array.index(i) != 0 and shuffled_array.index(i) % 2 == 0:
            mult *= i
    
    conc = str(shuffled_array[0]) + str(shuffled_array[-2])

    print(mult)
    print(conc)

some_func(some_array)