#Accept age of a person. If age is less than 18, print minor otherwise Major.

def age():

    a = int(input("Enter age "))

    if(a <= 18):
        print("minor")

    else:
        print("major")

age()
