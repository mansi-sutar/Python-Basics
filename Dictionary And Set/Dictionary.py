# Creation of Dictionary
Names = {1: 'Mansi', 2: 'Riya', 3: 'Priya', 4: 'Siya'}
print(Names)

# Creation of Dictionary with dict() method
Dict = dict({1: 'Meera', 2: 'For', 3: 'Sameera'})
print(Dict)

# Creation of  Dictionary with each item as a Pair
Dict = dict([(1, 'Vina'), (2, 'Mina')])
print(Dict)

# Nested Dictionary
Dict = {1: 'Mansi', 2: 'Pooja',3: {'A': '101', 'B': '102', 'C': '103'}}
print(Dict)

# accessing a element of dictionary
print(Dict[1])

# accessing a element using get() method
print(Dict.get(2))

# demo for all dictionary methods
dict1 = Names = {1: 'Mansi', 2: 'Riya', 3: 'Priya', 4: 'Siya'}

# copy() method
dict2 = dict1.copy()
print(dict2)

# clear() method
dict1.clear()
print(dict1)

# get() method
print(dict2.get(2))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Meera"})
print(dict2)

# values() method
print(dict2.values())