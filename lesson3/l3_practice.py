
try:
    a = int(input("Side A:"))
    b = int(input("Side B:"))
    c = int(input("Side C:"))

    if (a + b) > c:
        if (a + c) > b:
            if (b + c) > a:
                print("Triangle exists")
            else:
                print("Triangle doesn't exist")
        else:
            print("Triangle doesn't exist")
    else:
        print("Triangle doesn't exist")

    # if (a + b) > c and (a + c) > b and (b + c) > a:
    #     print("Triangle exists")
    # else:
    #     print("Triangle doesn't exist")
except ValueError:
    print("Please try again and type integers!")

