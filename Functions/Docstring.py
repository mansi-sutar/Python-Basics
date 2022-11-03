def fun():
    """Function to check if the number is even or odd"""
    num = input("Enter no.:")
    if (num % 2 == 0):
        print("even")
    else:
        print("odd")
print(fun.__doc__)