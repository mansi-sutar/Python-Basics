file = open("Data.txt", "w")
file.write("Welcome...")

file = open("Data.txt", "r")
print(file.read())

file.close()

