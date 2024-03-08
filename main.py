import os

p = "C:\\Users\\Admin\\desktop"
def music():
    folder_name = "Music"
    folder_path = p
    path = os.path.join(folder_path, folder_name)
    return path

Music_folder = music()


check = os.listdir(p)

for a in check:
    # extension = a.split('.')[-1]
    # print("[" + a + "]",end="")
    if "Music" not in a:
        os.mkdir(Music_folder)
    else:
        print("That folder exist.")
    # elif extension == "txt":
    #     print(" is a text file")
    # elif extension == "url":
    #     print(" is a url file")
    # else:
    #     print(" is a exe file")



# file = "test.1.txt"
# name = file.split('.')[-1]
#
# print(name)