# Seil Tekinaeva
# Date: March 4, 2026
# Problem 3: Multiply all numbers in a list

def multiplyList(numbers):
    result= 1
    for num in numbers:
        result= result * num

    return result
myList = [5, 2, 7, -1]
answer= multiplyList(myList)
print("The multiplication result is:", answer)
