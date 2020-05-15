def gen(n):
    for i in range(n):
        yield i

g = gen(89)
print(g.__next__())
print(g.__next__())
print(g.__next__())

for i in g:
    print(i)
    
d = "darkweb"
ier = iter(d)

print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())


print("\nFor learn how to run and access genrators , open this file in your editor and learn about this file")
print("\nThank You\n")
