# def factorial(n):
#     assert n>=0 and int(n)==n, 'The number must be positive integer only'
#     if n==0 or n==1:
#         return 1
#     else:
#         result = n*factorial(n-1)
#         return result
#
# print(factorial(5))

def powOfTwo(n):
    if n<=0:
        return 1
    else:
        power = powOfTwo(n-1)
        return power*2

print(powOfTwo(4))