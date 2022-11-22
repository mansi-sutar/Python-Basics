'''
Assignment Q.1
[
{'name':'jenine','role':'developer', age:'32'},
{'name':'Manish','role':'junior developer', 'age':'21'},
{'name':'sunil','role':'senior developer','age':'19'},
{'name':'anil','role':'senior developer','age':'40'},
{'name':'john','role':'senior developer','age':'28'}
]
Sort this list on base of age.'''
# sort(reverse=True|False, key=sortFunction)

lst = [
        {'name':'jenine','role':'developer', 'age':'32'},
        {'name':'Manish','role':'junior developer', 'age':'21'},
        {'name':'sunil','role':'senior developer','age':'19'},
        {'name':'anil','role':'senior developer','age':'40'},
        {'name':'john','role':'senior developer','age':'28'}
      ]

def get_age(lst):
    return lst.get('age')
lst.sort(key=get_age)
print(lst)

# Using lambda function
print("\n Sorting using lambda function...!")
lst.sort(key=lambda age: age['age'])
for i in lst:
    print(i)

# Sorting in reverse order
print("\n Sorting in reverse order...!")
lst.sort(reverse=True,key=get_age)
for i in lst:
    print(i)

