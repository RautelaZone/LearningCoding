def fact(n):
    assert n>=0 and int(n)==n, 'Number must be positive integer only'
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

no = int(input("Enter a no :"))
value=fact(no)
print("Factorial of",no, "is:", value)