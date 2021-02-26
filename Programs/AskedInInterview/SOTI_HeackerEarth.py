'''
The following two were given for practice
'''

def add(a,b):
    assert(a>b)
    assert(b>a)
    print(a/b)
add(4,0)
#Output : Assertion Error

class A:
    def __init__(self,s):
        self.s=s

    def print(self):
        pass

a = A('John')
a.print()

##########################################################################


