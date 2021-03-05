a=[1,3,5,1,5,7,8]
b=[1,2,6,3,4]

result=list(filter(lambda item: item in a, b))
print("Common values are", result)