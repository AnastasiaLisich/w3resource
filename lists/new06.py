x = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last_sort(tuple1):
    return tuple1[-1]

x.sort(key=last_sort)

print(x)

