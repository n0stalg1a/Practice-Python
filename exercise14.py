# 14: List Remove Duplicates
# Write a program (function!) that takes a list and returns a new list that
# contains all the elements of the first list minus all the duplicates.

# Extras:
# Write two different functions to do this - one using a loop and constructing
# a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in
# a different function.

a = [1, 1, 1, 2, 2, 2, 3, 3, 3]


def removeduplicatesloop(list):
    b = []
    for i in list:
        if i not in b:
            b.append(i)
    return b


def removeduplicatesset(list):
    return set(list)


print(removeduplicatesloop(a))
print(removeduplicatesset(a))
