x = int(input("X: "))
y = int(input("Y: "))

if x == 0 and y == 0:
    print('The point is origin')
elif x == 0 and y != 0:
    print('The point is on the X axis')
elif x != 0 and y == 0:
    print('The point is on the Y axis')
elif x > 0 and y > 0:
    print('The point is on the I quarter')
elif x > 0 and y < 0:
    print('The point is on the II quarter')
elif x < 0 and y < 0:
    print('The point is on the III quarter')
elif x < 0 and y > 0:
    print('The point is on the IV quarter')
