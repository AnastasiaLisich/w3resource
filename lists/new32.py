# Write a Python program to check whether a list contains a sublist.

x = ['A', 'B', 'C', 'D', 'E']
y = ['C', 'D']


def find(lst, sub):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j+1]
            if sublist == sub:
                return True
    return False


if find(x, y):
    print('Found')
else:
    print('Not found')




