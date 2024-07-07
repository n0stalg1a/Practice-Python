# 2: Odd or Even
# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd 
# number react differently when divided by 2?

# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.

usernum = int(input('Please enter a number: '))
divisor = int(input('Please enter a number to divide it by: '))

if usernum % 4 == 0:
    print('Number is divisible by 4 and is even.')
elif usernum % 2 == 0:
    print('Number is even.')
else:
    print('Number is odd.')


if usernum % divisor == 0:
    print(f'The number {usernum} is divisible by {divisor}.')
else:
    print(f'The number {usernum} is not divisible by {divisor}.')