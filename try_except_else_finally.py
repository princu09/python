f1 = open("textfile.txt")

try:
    f = open("textfile2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    f.close()
    f1.close()

print("Important stuff")


# -------------------------Note------------------------------------

print("\n-------------------------------------------------------------------------------------------------------------------")
print("\nFor learn how to run and access  try_except_else_finally , open this file in your editor and learn about this file")
print("\nThank You\n")