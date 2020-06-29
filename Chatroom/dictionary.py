import time

Dict = { }
print("Created an empty dictionary")
print(Dict)


Dict = dict({'1': 'Hello', '2': 'Deepen'})
print("Added some content to it using dict() function")
print(Dict)

Dict [3] = 'Parmar'
print("Adding new elements to the dictionary")
print(Dict)

print("Accessing a element using get() function")
print(Dict.get(3))

del Dict[3]
print(" Deleting element from the dictonary")
print(Dict)


print("Printing values of the key")
for k in Dict:
    print(k)

Dict.clear()
print("Deleting the entire Dictionary")
print(Dict)


# Exploring the time class
print(" Start: %s", time.ctime())
time.sleep(5)
print(" Stop: %s", time.ctime())

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("current time: %s", current_time)

# Append Dictionary with for loop 
