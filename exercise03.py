# 3: List Less Than Ten
# Write a program that prints out all the elements of the list that are less than 5.

# Extras:
# Instead of printing the elements one by one, make a new list that has all the 
# elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from 
# the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

# Extra 1 and 3
usernum = int(input('Please select a number to check for numbers below it in a list: '))

for i in a:
    if i < usernum:
        b.append(i)

print(b)

# All Extras
print([i for i in a if i < usernum])