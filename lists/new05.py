# Write a Python program to count the number of strings where the string length is 2 or more and the first
# and last character are same from a given list of strings.


sample_list = ['abc', 'xyz', 'aba', '1221', '', 'a', '12', 'bb', '']
count = 0
for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
print(temp)



