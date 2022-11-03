# if statement
num = 8
if num % 2 == 0:
    print("Numbers is Even")

# if else stmt
num = int(input("Enter no."))
if num % 2 == 0:
    print("Numbers is Even")
else:
    print("Numbers is Odd")

# elif stmt
marks = int(input("Enter your marks to check grades...!!!"))
if marks >= 85:
    print("Grade : A++")
elif marks >= 75 and marks < 85:
    print("Grade : A+")
else:
    print("Grade : A")

# Nested if
num = int(input("Enter no. :"))
if num < 100:
    if num % 2 == 0:
        print("Numbers is Even")


