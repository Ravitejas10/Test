from collections import Counter

s1=Counter([1,2,1,2,2,1,2,1,2,2,1])
print(s1)

#OrderedDict : it remembers the order in which the keys were inserted.
from collections import OrderedDict
d1= OrderedDict()
d1['lm']=10
d1['r']=8
d1['v']=9

for k,v in d1.items():
    print(k,v)

d1.pop('lm')
print(d1)
d1['lm']=10
print(d1)

#DefaultDict is used to provide some default values for the key that does not exist and never raises a KeyError
from collections import defaultdict

d2=defaultdict(int)
l=['lm','r','v','v','lm','v']
for i in l:
    d2[i]+=1   #The default value is 0 so there is no need to enter the key first

print(d2)

#ChainMap
#A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries. When a key is needed to be found then all the dictionaries are searched one by one until the key is found

from collections import ChainMap
d3={'a':2,'b':5}
d4={'f':5,'n':4}
d5={'m':10,'r':8}

b=ChainMap(d3,d4,d5)
print(b)
print(b['a'],b['m'])