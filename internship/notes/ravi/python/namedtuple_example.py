from collections import namedtuple
s=namedtuple("Student",["name","club"])
s1=s("rt","barca")
s2=s("prath","madrid")

print(s1[0])
print(s1.name)
