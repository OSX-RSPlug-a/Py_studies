

day_number = int(input("\n Enter your choice of a number of day's week =  \n"))

def days_of_week(day_number):
    days_of_week = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    
    print(days_of_week.get(day_number, "Invalid day number"))
    

days_of_week(day_number) 