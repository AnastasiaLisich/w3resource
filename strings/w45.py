# 45. Write a Python program to check if a string contains all letters of the alphabet.

the_phrase = 'A winter spruce in the forest'

test_phrase = 'The quick brown fox jumps over the lazy dog'

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def check_all_letters(the_str):
    for letter in alphabet:
        if letter not in the_str.upper():
            return False
    return True

print(check_all_letters(the_phrase))
print(check_all_letters(test_phrase))


def check(string):
    return not bool(set(alphabet) - set(string.upper()) - {' '})

print(check(the_phrase))
print(check(test_phrase))
