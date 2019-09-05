try:
    a = input("a:")
    b = input("b:")
    c = input("c:")

    a = int(a)
    b = int(b)
    c = int(c)

    if a <= b and a <= c:
        min = a
    elif b <= a and b <= c:
        min = b
    elif c <= a and c <= b:
        min = c

    if a >= b and a >= c:
        max = a
    elif b >= a and b >= c:
        max = b
    elif c >= a and c >= b:
        max = c

    print("Min is:", min, " and max is:", max)
except ValueError:
    print(a, b ,c)