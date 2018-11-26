# Write a Python program to find the second smallest number in a list

the_list = [1, 100, -50, 90, 2, 0, -7575]

x = min(the_list)
the_list.remove(x)
y = min(the_list)
print(y)



# smallest = None
# second_smallest = None
# for item in the_list:
#     if smallest is None:
#         smallest = item
#         continue
#     if item < smallest:
#         second_smallest = smallest
#         smallest = item

# print(second_smallest)






