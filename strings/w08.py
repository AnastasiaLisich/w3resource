# Write a Python function that takes a list of words and returns the length of the longest one.

list_of_strings = ['Abracadabra', 'Aloha Hawaii', 'Encyclopedia Britannica']

def get_longest_string(lst):
    longest = ''
    for string in lst:
        if len(string) > len(longest):
            longest = string
    return len(longest)

print(get_longest_string(list_of_strings))


answer = max(len(x) for x in list_of_strings)
print(answer)
