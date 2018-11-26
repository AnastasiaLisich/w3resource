# Write a Python function that takes a list of strings and returns the longest one.
# If there are multiple strings with the same length, print them all.
# Example:
# Input: AA BCD ABCD A DEFG ERF
# Answer: ABCD DEFG

list_of_strings = ['Abrac', 'AbracadabraAbr', 'Gritannica', 'Abrac', 'Pritannica', 'Abracad']


# def get_longest_string(lst):
#     longest = ''
#     for string in lst:
#         if len(string) > len(longest):
#             longest = string
#     return longest


def get_longest_strings(lst):
    list_of_longest = []
    for string in lst:
        if not list_of_longest or len(string) == len(list_of_longest[0]):
            list_of_longest.append(string)
        elif len(string) > len(list_of_longest[0]):
            list_of_longest = [string]
    return list_of_longest

# print(get_longest_string(list_of_strings))
print(get_longest_strings(list_of_strings))

