import math


a = int(input("Type a number for a \n"))

b = int(input("Type a number for b \n")) 

c = int(input("Type a number for c \n"))  

delta = (b**2) - (4 * a * c)

if delta < 0:
    print('No real roots')
else:
    print("Result of delta is: ", delta)

    root = math.sqrt(delta)

    x = (-b + root) / (2 * a)

    y = (-b - root) / (2 * a)
    
    print("x1 will be: \n", x)

    print("x2 will be: \n", y)




