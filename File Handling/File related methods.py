file = open("Data2.txt", "r")
print(file.read())

# tell() : It returns the current position of the file pointer within the file.
print(file.tell())

# fush() : It flushes the internal buffer.
print(file.flush())

# fileno() : It returns the file descriptor used by the underlying implementation to request I/O from the OS.
print(file.fileno())

# close() : It closes the opened file.
file.close()