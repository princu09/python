ls =[]

# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# print(ls)

# -------------------------List Comprehension------------------------------------

ls = [i for i in range(100) if i%3==0]

print(ls ,"\n")

# -------------------------Dictionary Comprehension------------------------------------

dict1 = {i:f"item{i}" for i in range(51) if i%5==0}
print(dict1 ,"\n")

# -------------------------Reverse Dictionary Comprehension------------------------------------

dict1 = {i:f"item {i}" for i in range(51) if i%5==0}
dict1 = {value:key for key,value in dict1.items()}
print(dict1 ,"\n")

# -------------------------Set Comprehension------------------------------------

dresses = {dress for dress in ["yellow dress" , "yellow dress" , "red dress", "red dress", "red dress" , "pink dress"]}
print(dresses)

# -------------------------Gentator Comprehension------------------------------------

evens = (i for i in range(100) if i%2==0)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

# for item in evens:
#     print(item)

# -------------------------Note------------------------------------

print("\n-------------------------------------------------------------------------------------------------------------------")
print("\nFor learn how to run and access list comprehensions , open this file in your editor and learn about this file")
print("\nThank You\n")