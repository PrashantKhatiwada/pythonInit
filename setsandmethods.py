a1 = {3, 5, 23, 5, 5, 5}
a2 = {3, 5, 23}
a3 = {43, 34, 25, 3, 5}

print(a2.union(a3))
print(a2.intersection(a3))
a2.intersection_update(a3)
print(a2)

print(a1 == a2)  # true
# print(a1.pop())
# a1.clear()

a1.add(22)
print(a1)

# print(a1)

print(a2)

print(a1 == a2)  # false

set1 = set([1,2,3,4,5]) # Set Constructor
print(set1)







