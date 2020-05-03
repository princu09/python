#File Open py file

f = open("textfile.txt")

content = f.read()

for line in content:
    print(line)

print("open this file to learn how to use and execute file.")
f.close()
