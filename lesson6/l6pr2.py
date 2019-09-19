def positive():
    print('Положительное')

def negative():
    print('Отрицательное')

def test():
    try:
        number = float(input("Введите число: "))
        if number > 0:
            positive()
        elif number < 0:
            negative()
        else:
            print("Это 0!")
    except ValueError:
        print("Необходимо ввести число!")
        test()

test()