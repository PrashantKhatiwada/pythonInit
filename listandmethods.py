l1 = [1, 3, 434, 343, 23, "Prashant"]
l2 = [10, 12, 65, 23, 1211, 434, 25]
print(type(l1))
print(l1)
l1.remove(3)
l1.remove("Prashant")
print(l1)
print(l1.count(343))
l2.sort()
print(l2)
l2.pop()
print(l2)
l2.append(99)
print(l2)
l2.extend([2, 343, 23, 34343])
l2.sort()
print(l2)
l2.clear()
print(l2)
print(l1.index(343))

list1 = list([1,2,3,4,5]) # List Constructor
print(list1)
