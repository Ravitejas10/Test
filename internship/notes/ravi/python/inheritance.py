class Student:
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    def isemp(self):
        return False

class emp(Student):
    def __init__(self,name):
        self.name=name
    def isemp(self):
        return True

s1=Student("ravi")
print(s1.isemp())
s2=emp("snigdha")
print(s2.getname())
print(s2.isemp())
