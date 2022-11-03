#r: open an existing file for a read operation.
file = open("Data.txt", "r")
print(file.read())

# w: open an existing file for a write operation.
file = open("Data.txt", "w")
file.write("\nThis is the write command")

# a: open an existing file for append operation.
file = open('Data.txt', 'a')
file.write("\nThis is append cmd")

# r+: To read and write data into the file.
file = open("Data.txt", "r+")
print(file.read())
file.write("\nThis is the read n write command")

# w+: To write and read data.
file = open("Data.txt", "w+")
file.write("\nThis is the write n read command")
print(file.read())

# a+: To append and read data from the file.
file = open("Data.txt", "a+")
file.write("\nThis is the a+ command")
print(file.read())















