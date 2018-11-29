# Write a Python program to reverse words in a string.

string = 'Kirill Kondratenko'


def reverse_string(string):
    return ''.join(reversed(string))


def reverse_words(any_str):
    new_list = string.split()
    temp = ''
    for word in new_list:
        temp += reverse_string(word) + ' '
    return temp[:-1]


print(reverse_words(string))


# print(' '.join(''.join(reversed(w)) for w in string.split()))
