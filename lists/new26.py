# Write a python program to check whether two lists are circularly identical.

x = ['A', 'B', 'C', 'D', 'E']
y = ['D', 'E', 'A', 'B', 'C']

def rotate(lst, n):
    if n == 0:
        return lst
    return lst[-n:] + lst[:len(lst) - n]

if any(rotate(x, k) == y for k in range(len(x))):
    print('BINGO')
else:
    print('FAIL')

