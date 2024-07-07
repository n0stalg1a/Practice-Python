# 13: Fibonacci
# Write a program that asks the user how many Fibonnaci numbers 
# to generate and then generates them. Take this opportunity to 
# think about how you can use functions. Make sure to ask the user 
# to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the 
# next number in the sequence is the sum of the previous two numbers 
# in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def startsequence():
    a = int(input('Please enter a number of Fibonacci sequence numbers to generate: '))
    if a <= 0:
        b = []
        print(b)
    elif a == 1:
        b = [1]
        print(b)
    elif a == 2:
        b = [1, 1]
        print(b)
    else:
        b = [1, 1]
        for i in range(2, a):
            b.append(b[i - 1] + b[i - 2])
        print(b)

startsequence()