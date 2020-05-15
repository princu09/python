import time
from functools import lru_cache

@lru_cache(maxsize=32)

def some_work(n):
    #some task taking n seconds
    time.sleep(n)
    return n

if __name__ == "__main__":
    
    print("Now running some one work")
    some_work(3)
    some_work(2)
    some_work(5)
    some_work(8)
    print("Done... Calling again")
    some_work(3)
    print("Called Again")


# -------------------------Note------------------------------------

print("\n-------------------------------------------------------------------------------------------------------------------")
print("\nFor learn how to run and access else with for loops , open this file in your editor and learn about this file")
print("\nThank You\n")