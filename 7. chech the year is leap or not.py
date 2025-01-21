#Accept a year value from the user. Check whether it is a leap year or not.

def year():
    
    a = int(input("Enter a year "))

    if(a % 4 == 0 or a % 400 == 0 or a % 100 == 0):
        print("The given year is leap year")

    else:
        print("The given year is not leap year")

year()
year()
year()
