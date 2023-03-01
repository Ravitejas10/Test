class A:
    def __init__(self):
        self.val=10
    def display(self):
        print(self.val)

class B(A):
    def __init__(self):
        self.val=11
    def display(self):
        print(self.val)

c1=A()
print(c1.display())
c2=B()
print(c2.display())