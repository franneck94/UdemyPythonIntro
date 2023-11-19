name = "Jan Maximilan Schaffranek"


result = name.find("an")

if result == -1:
    print("Not found")
else:
    print("Found at index: ", result)


name2 = name.replace("Jan", "Yann")
print(name)
print(name2)


name3 = name.upper()
print(name3)


name4 = name.lower()
print(name4)


name5 = name.split(" ")
print(name5)


count = name.count("an")
print(count)
