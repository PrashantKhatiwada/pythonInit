# Variables Assignment

x = 5
y = "john"
print(x)
print(y)

# Casting

x = str(4)
y = int('3')
z = float(4)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

# name = "Prashant"

# is same as

# name = 'Prashant'

# Variables are Case-Sensitive

# a is not same as A

# Assigning multiple values

a, b, c = "Ram", "Shyam", "Hari"

print(a)
print(b)
print(c)

# One value to multiple variables

d = e = f = 24

print(d)
print(e)
print(f)

# unpacking a list

aList = ["Apple", "Orange", 21]
p, q, r = aList
print(p)
print(q)
print(r)

# Global Variables



def simpleFunc():
    global my_name
    my_name = "Prashant"
    print(my_name)

simpleFunc()
print(my_name)

# Joining different dataTypes

print(my_name, x) # , gives a space
print(my_name + x) # + does not
