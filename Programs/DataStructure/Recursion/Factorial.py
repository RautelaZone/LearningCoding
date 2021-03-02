def fact(n):
    if n in [0,1]:
        return 1
    else:
        return n*fact(n-1)

no = int(input("Enter a number :"))
if no<=0 or no!=int(no):
    print("Number must be positive integer only.")
else:
    value=fact(no)
    print("Factorial of",no, "is:", value)