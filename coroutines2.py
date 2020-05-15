
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on dark web"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("dark")

search.close()

# -------------------------Comment out one by one and run then learn------------------------------------

# search.send("dark")

# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")



# -------------------------Note------------------------------------

print("\n-------------------------------------------------------------------------------------------------------------------")
print("\nFor learn how to run and access  coroutine , open this file in your editor and learn about this file")
print("\nThank You\n")