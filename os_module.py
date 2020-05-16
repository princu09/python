import os

# --------------------------Create a single folder-------------------------------
os.mkdir("single")

# --------------------------Create a folder and subfolder-------------------------------
os.makedirs("Main/sub folder")

# --------------------------Open any file from current location-------------------------------
f = open("textfile.txt")
f.close()

# --------------------------Rename any file-------------------------------
os.rename("mk.txt" , "change.txt")

# --------------------------Get Environment variable-------------------------------
print(os.environ.get('Home'))

# --------------------------If path exists print true else print false-------------------------------
print(os.path.exists("ReadMe.txt"))
print("")
print(os.path.exists("ReadMe2.txt"))

# --------------------------If directory exists print true else print false-------------------------------
print(os.path.isdir("log.txt"))
print("")

# --------------------------If directory exists print true else print false-------------------------------
print(os.path.isfile("mylogs.txt"))


# -------------------------Note------------------------------------

print("\n-------------------------------------------------------------------------------------------------------------------")
print("\nFor learn how to run and access os module, open this file in your editor and learn about this file")
print("\nThank You\n")