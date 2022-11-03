# Finally Keyword
def div(a,b) :
    try:
        r = a // b
        print(r)
    except ZeroDivisionError:
        print("Can't divide by zero")
    finally:
        print('This is always executed')
div(2,4)

div(4,0)

# Raising exception
arr = [1,2,3,4,5]
if len(arr) > 4:
    raise Exception("Length of the given list must be less than or equal to 4")