def recur_fibo(n):
    if n in [0,1]:
        return n
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

no = int(input("Enter the number till which need to show Fibonacci: "))

if no<=0 or no!=int(no):
    print("Number must be positive integer only.")
else:
    print("Fibonacci series is: ")
    for i in range(no):
        print(recur_fibo(i),end=" ")