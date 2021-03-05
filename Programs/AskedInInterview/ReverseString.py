
# Using For Loop
name="AnilRautela"
str=""
for i in name:
    str=i+str
print("The reverse string using loop:",str)

# Using Slicing
name="AnilRautela"
print("The reverse string using slicing:",name[::-1])


#Using in-build function
name= "AnilRautela"
print("The reverse string using BIF:","".join(reversed(name)))

#Using recursion
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:]) + s[0]

name="AnilRautela"
print("The reverse string using Recursion:",reverse(name))
