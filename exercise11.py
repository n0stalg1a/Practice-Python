# 11: Check Primality Functions
# Ask the user for a number and determine whether the number is prime or not.

import random

USER_NUM = random.randint(1, 20)

if USER_NUM == 2:
    b = f'Number {USER_NUM} is prime!'
elif USER_NUM == 1:
    b = f'Number {USER_NUM} is not prime.'
else:
    for i in range(2, USER_NUM):
        if USER_NUM % i == 0:
            b = f'Number {USER_NUM} is not prime.'
            break
    else:
        b = f'Number {USER_NUM} is prime!'

print(b)
