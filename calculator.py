# s simple calculator to exercise programming

def som(x, y):
    return x+y

def sub(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x, y):
    if y==0:
        return "This terms are not aplied to division by zero"
    return x/y

def square(x, y):
    return x**y

print("\n ########################### Calcaulator ########################### \n")

while True:
    print("Insert number 1 to add sum \n")
    print("Insert number 2 to subtract \n")
    print("Insert number 3 to multiply \n")
    print("Insert number 4 to devide \n")
    print("Insert number 5 to square of \n")
    print("Insert number 6 to Exit \n")
    
    choice = int(input("\n Enter your choice =  \n"))
    
    if (choice == 1):
        n1 =  int(input("\n Insert you first number =  \n"))
        n2 =  int(input("\n Insert you second number =  \n"))
        print("\n ######## Result: ", som(n1, n2), " #######\n")
    elif (choice == 2):
        n1 =  int(input("\n Insert you first number =  \n"))
        n2 =  int(input("\n Insert you second number =  \n"))
        print("\n ####### Result: ", sub(n1, n2), " #######\n")
    elif (choice == 3):
        n1 =  int(input("\n Insert you first number =  \n"))
        n2 =  int(input("\n Insert you second number =  \n"))
        print("\n ####### Result: ", mult(n1, n2), " #######\n")
    elif (choice == 4):
        n1 =  int(input("\n Insert you first number =  \n"))
        n2 =  int(input("\n Insert you second number =  \n"))
        print("\n ####### Result: ", div(n1, n2), " #######\n")
    elif (choice == 5):
        n1 =  int(input("\n Insert you first number =  \n"))
        n2 =  int(input("\n Insert you second number =  \n"))
        print("\n ####### Result: ", square(n1, n2), " #######\n")
    elif (choice == 6):
        break
    else:
        print("\n ####### !!! Please. Insert a valid number's choice !!! ####### \n")
