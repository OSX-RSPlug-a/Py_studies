import sys

def triangulo01():

    rows = 5

    for i in range(0, rows)[::-1]:
        for j in range(0, i +1):
            print("*", end=' ')
        print("\r")


def triangulo02():

    rows = 5

    for j in range(1, rows+1):
        print("* " * j)


def triangulo03():

    rows = 5

    for i in range(rows+1, 0, -1):
        for j in range(0, i -1):
            print("*", end=' ')
        print(" ")



def triangulo04():

    rows = 5
    k = 2 * rows -2

    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k +1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")


print()

print("#########################TRIANGULOS##########################")

print()

triangulo01()

print()

triangulo02()

print()

triangulo03()

print()

triangulo04()

print()