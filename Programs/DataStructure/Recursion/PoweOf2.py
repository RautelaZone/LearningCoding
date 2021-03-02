def powOfTwo(n):
    if n<=0:
        return 1
    else:
        power = powOfTwo(n-1)
        return power*2

no=int(input("Enter a number: "))
print("Power of 2^"+str(no),"is:",powOfTwo(no))