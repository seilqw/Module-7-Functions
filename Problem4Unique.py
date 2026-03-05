#  Seil Tekinaeva
# Date: March 4, 2026
# Problem 4: Return a list with unique elements

def uniqueList(numbers):

    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique


myList = [1, 3, 3, 3, 6, 2, 3, 5]

result = uniqueList(myList)
print("Unique list:", result)
