import time

initial = time.time()
#print(initial)

k = 0
while(k<45):
    print("This is Dark Web")
    k+=1

print("While Loop run in ", time.time() - initial , "seconds")


initial2 = time.time()
for i in range (45):
    print("This is Dark Web")

print("While Loop run in ", time.time() - initial2, "seconds")