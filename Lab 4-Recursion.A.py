def Recursion(n, a=1):
    if (n==0):
        return a
    else:
        return Recursion(n-1, n*a)

number = 7

if number < 0:
    print("It must be a positive Integer.")
elif number == 0:
    print("The Factorial of the od number 0 is 1")
else:
    print("The Factorial of number", number, "is equal to", Recursion(number))