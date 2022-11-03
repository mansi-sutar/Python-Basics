# Creation of set
set1 = set("MansiSutar")
print(set1)

# Accessing element
set2 = set(["Mansi", "Priya", "Meera", "Jiya","Kiya"])
# for loop
for i in set2:
    print(i, end=" ")

# Checking the element  using in keyword
print("Jiya" in set2)

# Set method

# add()
set2.add("Siya")
print("\n")
for i in set2:
    print(i, end=" ")

# update()
set2.update(["Heena"])
print("\n")
for i in set2:
    print(i, end=" ")

# discard()
set2.discard("Jiya")
print("\n")
for i in set2:
    print(i, end=" ")

# copy
set3 = set2.copy()
print("\n")
for i in set3:
    print(i, end=" ")




