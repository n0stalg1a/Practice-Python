# 11: Check Primality Functions
# Ask the user for a number and determine whether the number is prime or not.

import random

usernum = random.randint(1, 20)

if usernum == 2:
    b = f'Number {usernum} is prime!'
elif usernum == 1:
    b = f'Number {usernum} is not prime.'
else:
    for i in range(2, usernum):
        if usernum % i == 0:
            b = f'Number {usernum} is not prime.'
            break
    else:
        b = f'Number {usernum} is prime!'

print(b)