# dict1 = {} # empty dictionary
# print(type(dict1))
# set1 = set() # to create an empty set
# print(type(set1))

myDetails = {"name": "Prashant", "subject": "CS", "school": "Caldwell University"}

print(myDetails["name"])
myDetails["Address"] = "Urlabari"
print(myDetails)

print(myDetails.get("subject"))
dict1 = dict(Hello = "Greeting", name = "Identity") # Dictionary Constructor
print(dict1)
print(myDetails.keys())
print(myDetails.values())
print(myDetails.items())
print(type(myDetails.items()))

#copying a dictionary

dict2 = dict1.copy()
print(dict2)

# Nested Dictionary

dict3 = {
    "std1": {
        "name": "Prashant",
        "marks": 99
    },

    "std2": {
        "name": "Ram",
        "marks": 10
    }
}

print(dict3)
print(dict3['std1']['name']) # accessing a nested loop item


