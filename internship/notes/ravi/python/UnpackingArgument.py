def student(name,usn):
    print(name,usn)

student1=["ravi",99]
#Functions calls can be made with *-operator to unpack the arguments out of a list or tuple.
student(*student1)
student2={"name":"snigdha","usn": 1}
## Functions calls can be made with **-operator to unpack the arguments out of a dictionary
student(**student2)