#Since filter() only keeps elements where it produces True

li=[32,12,546,879,234,123,234,36,67]
l1=list(filter(lambda x:(x%2!=0) , li))
print(l1)


l2=list(map(lambda x:x*2,li))
print(l2)

from functools import reduce
t1= reduce(lambda x,y:x+y,li)
print(t1)

