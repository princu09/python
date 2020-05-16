import pickle

# pickling a python object

# ------------------------Create a pickle file--------------------------------
cars = ["audi", "bmw", "maruti 800"]
file = "mycar.pkl"

fileobj = open(file ,'wb')
pickle.dump(cars , fileobj)

fileobj.close()

# ------------------------Extract pickle file--------------------------------
file = "mycar.pkl"
fileobj = open(file , 'rb')
mycar = pickle.load(fileobj)

print(mycar)

# -------------------------Note------------------------------------

print("\nFor learn how to run and access pickle , open this file in your editor and learn about this file")
print("\nThank You\n")