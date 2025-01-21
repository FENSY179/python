#Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter

def rec():
    
    L = float(input("Enter number of length "))
    W = float(input("Enter number of width "))
    A = L * W
    P = 2 * (L+W)

    if(A>P):
        print("Area of Rec is greater than it's Perimeter")

    elif(A==P):
        print("Area is equal to Perimeter")

    else:
        print("Perimeter is greater than Area")

rec()
rec()
rec()
