hours_worked = float(input("Insert the worked hours: "))
val_hour = float(input("Insert the valuer per hour: "))

if (hours_worked >= 100):
    bonus = 500.00
else:
    bonus = 0


salary = hours_worked * val_hour + bonus

print(f"The salary for the worked hours and possible plus hour in this week is: {salary}")