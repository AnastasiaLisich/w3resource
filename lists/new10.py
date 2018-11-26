 # Write a Python program to find the list of words that are longer than n from a given list of words.

lst1 = ['Hello, winter!', 'Goodbye, autumn!', 'Merry Christmas!', 'Happy New Year!']
n = 14
lst2 = []

def longer_words(lst1, n):
    for string in lst1:
        if len(string) > n:
            lst2.append(string)
    return lst2

longer_words(lst1, n)
print(lst2)

lst3 = [s for s in lst1 if len(s) > n]
print(lst3)








