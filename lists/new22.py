# Write a Python program to find the index of an item in a specified list.

list0 = ['a', 1, 'b', 2]
querylist = ['b', '4', 'c', 'd', 2]
# num = -1
# if elem in list0:
#     for temp in list0:
#         num = num + 1
#         if temp == elem:
#             break
#     print(num)
# else:
#     print('Not found')

for elem in querylist:
    try:
        print(list0.index(elem))
    except ValueError:
        print('Not found')







