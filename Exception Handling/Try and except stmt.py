def div(x, y):
    try:
        result = x // y
        print("Result :", result)
    except ZeroDivisionError:
        print("Dividing by zero...!!! ")
div(4,2)
div(3,0)