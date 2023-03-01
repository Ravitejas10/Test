#The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.
# While list comprehension produces the entire list, generator expression produces one item at a time.

evens=[2,4,6,8,10]
# list comprehnsion
l1=[x**2 for x in evens]
print(l1)

#generators
l2=(x**2 for x in evens)
print(l2)
print(next(l2))
print(next(l2))
