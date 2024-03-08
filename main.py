import os

p = "C:\\Users\\Admin\\desktop"

check = os.listdir(p)

for a in check:
    extension = a.split('.')[-1]
    print("[" + a + "]",end="")
    if "." not in a:
        print(" is a folder")
    elif extension == "txt":
        print(" is a text file")
    elif extension == "url":
        print(" is a url file")
    else:
        print(" is a exe file")



# file = "test.1.txt"
# name = file.split('.')[-1]
#
# print(name)