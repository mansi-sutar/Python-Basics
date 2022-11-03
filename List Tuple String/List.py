# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [1, 2, 3, 4, 5, 6, 7, 8]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing using index
List = ["Mansi", "Priya", "Siya", "Jiya", "Kiya"]
print("\nList Items: ")
print(List)
print(List[2])

# Creating a List with duplicate values)
List = [1, 2, 3, 3, 4, 5]
print("\nList with duplicate value: ")
print(List)

# Creating a List with mixed type of values (Having numbers and strings)
List = [1, 'Sita', 2, 'Gita', 3]
print("\nList with the use of Mixed Values: ")
print(List)

# Accessing elements from list (Using Index)
print("Accessing a element from the list :")
print(List[0])
print(List[3])

# Accessing elements from a multi-dimensional list(Using Index)
List = [["Riya", "Priya", "Siya", "Jiya", "Kiya"], [1, 2, 3, 3, 4, 5]]
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][1])

# Accessing an element using negative indexing
List = [1, 2, 3, 4, 5, 6]
print("Accessing element using negative indexing")
print(List[-1])
# print the last element of list
print(List[-3])
# print the third last element of list

# Getting the size of Python list
print("Length of list :")
print(len(List))

# Taking Input of a Python List
'''string = input("Enter Items (Space-Separated): ")
# split the strings and store it to a list
lst = string.split()
print('The list is:', lst)'''

# Slicing of a List
List = [1, 2, 3, 4, 5, 6, 7, 8]
print("Initial List: ")
print(List)

Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)
# Printing elements from beginning till end
Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)

# Negative index List slicing
print("Initial List: ")
print(List)

# Print elements from beginning to a pre-defined point using Slice
Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)

# Print elements of a range using negative index List slicing
Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)

# Printing elements in reverse using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)



