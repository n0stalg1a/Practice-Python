# 6: String Lists
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

userinput = input('Please enter a word and I will check if it is a palindrome: ')

reversed = userinput[::-1]

print(reversed)

if userinput == reversed:
    print(f'The word {userinput} is indeed a palindrome.')
else:
    print(f'The word {userinput} is not a palindrome.')