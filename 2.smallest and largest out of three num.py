#Check whether a given number is odd or even.

a = float(input("Enter value of A "))
b = float(input("Enter value of B "))
c = float(input("Enter value of C "))

largest = a
if(b > largest):
    largest = b
if(c > largest):
    largest = c

smallest = a
if(b < smallest):
    smallest = b
if(c < smallest):
    smallest = c

print("largest num is",largest)
print("smallest num is",smallest)

    
