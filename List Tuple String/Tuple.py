# Creating a Tuple (string)
Tuple1 = ('Mansi','Riya','Priya','Siya')
print(Tuple1)

# Tuple with the use of built-in function
Tuple1 = tuple('Riya')
print(Tuple1)

# Tuple using list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# Tuple with Mixed Datatype
Tuple1 = (101, 'Riya', 102, 'Jiya')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Tuple with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Arya', 'Siya')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Accessing Tuple with Indexing
Tuple1 = tuple("Priya")
print("\nFirst element of Tuple: ")
print(Tuple1[0])

# Concatenation of tuples
Tuple3 = Tuple1 + Tuple2
print(Tuple3)

# Slicing of a Tuple
Tuple1 = tuple('MansiSutar')

# Removing First element
print("Removal of First Element: ")
print(Tuple1[1:])

# Reversing the Tuple
print("\nTuple after sequence of Element is reversed: ")
print(Tuple1[::-1])

# Printing elements of a Range
print("\nPrinting elements between Range 4-9: ")
print(Tuple1[1:5])

# negative indices
names = ('Mansi','Riya','Priya','Siya')
print("Element at -1 index: ", names[-1])
print("Elements between -4 and -1 are: ", names[-4:-1])

# Tuple Membership Test
# In operator
print('Mansi' in names)
print('Jiya' in names)

# Not in operator
print('Priya' not in names)
print('Meera' not in names)
