 # Write a Python program to check if the n-th element exists in a given list.
# the_list = []
the_list = [1, 4, 6, 90, 55, 'a']
n = -1


# try:
#     the_list[n]
# except IndexError:
#     print('not found')
# else:
#     print('found')


def check(lst, n):
    m = len(lst)
    return (n >= 0 and m > n) or (n < 0 and n >= -m)

print(check(the_list, n))
