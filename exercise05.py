# 5: List Overlap
# Write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your
# program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this
# out at this point - we’ll get to it soon)

import random

a = []
b = []


def createList(newlist):
    listlength = random.randint(10, 20)
    for i in range(1, listlength):
        num = random.randint(1, 25)
        if num not in newlist:
            newlist.append(num)


createList(a)
createList(b)
a.sort()
b.sort()
print(a)
print(b)


c = []

for i in a:
    for j in b:
        if j == i and j not in c:
            c.append(j)


print(c)


print(list(set(i for i in a if i in b)))
