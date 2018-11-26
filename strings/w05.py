# Write a Python program to get a single string
# from two given strings, separated by a space
# and swap the first two characters of each string.

str1 = 'Aloha'
str2 = 'Hawaii'

print(str2[0] + str2[1] + str1[2:] + ' ' + str1[:2] + str2[2:])

