import collections
de= collections.deque([1,2,3])
de.append(7)
print(de)
de.pop()
print(de)
de.appendleft(0)
print(de)
de.popleft()
print(de)

