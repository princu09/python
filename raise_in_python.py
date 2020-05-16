a =  input("what is your name ? \n")
b =  input("How much do you earn ?\n")

if int(b)==0:
    raise ZeroDivisionError("B is zero so stopping the program")

if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello ! {a} . You Earn {b}")


# ---------------------------Note-----------------------------------------
print("\ncheck this link : https://docs.python.org/3/reference/expressions.html")

print("\nFor learn how to run and access raise_in_python, open this file in your editor and learn about this file")
print("\nThank You\n")