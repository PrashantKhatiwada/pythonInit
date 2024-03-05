text = "Hi there, this is Prashant"

# Writing in a file

# with open("test.txt", "w") as f:
#     f.write(text)

# fp = open("test.txt","w")
# fp.write(text)
# fp.close()

# Reading a file

# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)

fp = open("test.txt", "r")
content = fp.read()
print(content)
fp.close()

# Appending to a file

# with open("test.txt", "a") as f:
#     f.write("\nI added this text later")

fp = open("test.txt", "a")
fp.write("\nI added this text more later")
fp.close()

