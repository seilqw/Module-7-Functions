# Seil Tekinaeva
# Date: March 4, 2026
# Problem 2: Check whether a number is in the range 1–10

def checkRange(num):
    if num in range(1,10):
        print(num, "is in the range")
    else:
        print(num, "is NOT in the range")

#testing
number = 7
checkRange(number)
