from datetime import datetime


now = datetime.now()

current_year = now.year

name = input("Insert your name: ")
age = int(input("Insert your age: "))

year = current_year - age

message = f"Hey, your name is {name} and you born in {year}"

print(current_year)
print(message)