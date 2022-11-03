'''input() function: It takes the value and type of the input you enter as it is without modifying any type.
raw_input() function: explicitly converts the input you give to type string,'''

# Using input()
val1 = input("Enter the name: ")
print(type(val1))
print(val1)

val2 = input("Enter the number: ")
print(type(val2))
val2 = int(val2)
print(type(val2))
print(val2)

# Using raw_input()
'''val1 = raw_input("Enter the name: ")
print(type(val1))
print(val1)

val2 = raw_input("Enter the number: ")
print(type(val2))
val2 = int(val2)
print(type(val2))
print(val2)'''
