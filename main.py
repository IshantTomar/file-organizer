import os

p = "C:\\Users\\Admin\\desktop\\test.txt"

if os.path.exists(p):
    print("That location exists.")
    if os.path.isfile(p):
        print("That is a file.")
else:
    print("That doesn't location exists.")