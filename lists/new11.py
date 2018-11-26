# Write a Python function that takes two lists
# and returns True if they have at least one common member.

list1 = ['a', 'b', 'c', 1, 2, 3]
list2 = ['a', 'c', 'e', 1, 3, 5]

def common_elem(list1, list2):
    intersection = set(list1) & set(list2)
    return bool(intersection)


    # for member1 in list1:
    #     for member2 in list2:
    #         if member1 == member2:
    #             return True
    # return False

print(common_elem(list1, list2))
