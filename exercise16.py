# 16: Password Generator
# Write a password generator in Python. Be creative with how you
# generate passwords - strong passwords have a mix of lowercase
# letters, uppercase letters, numbers, and symbols. The passwords
# should be random, generating a new password every time the user
# asks for a new password. Include your run-time code in a main method.

# Extra:
# Ask the user how strong they want their password to be. For weak
# passwords, pick a word or two from a list.

import string
import random

CHARS_LOWER = string.ascii_lowercase
CHARS_UPPER = string.ascii_uppercase
NUMS = string.digits
PUNCTUATION = string.punctuation

LENGTH = 14


def choosing_amount():
    return random.randint(2, 4)


def adding_to_password(char_list, passkey, count):
    for _ in range(choosing_amount()):
        if count < LENGTH:
            passkey += random.choice(char_list)
            count += 1
    return passkey, count


def cap_with_lowers(char_list, passkey, count):
    while count < LENGTH:
        passkey += random.choice(char_list)
        count += 1
    return passkey


def shuffler(word):
    return ''.join(random.sample(word, len(word)))


def generate_password():
    password = ''
    count = 0

    password, count = adding_to_password(CHARS_UPPER, password, count)
    password, count = adding_to_password(NUMS, password, count)
    password, count = adding_to_password(PUNCTUATION, password, count)
    password = cap_with_lowers(CHARS_LOWER, password, count)
    password = shuffler(password)

    return password


PASSWORD = generate_password()
print(PASSWORD)
