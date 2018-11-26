# Write a Python program to create a list
# by concatenating a given list which range goes from 1 to n

the_list = ['a', 'b', 'c']

# ['a0', 'b0', 'c0', 'a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3', 'a4', 'b4', 'c4', 'a5', 'b5', 'c5']

cycles = 6

def concaten_func(lst, n):
    combinations = []
    for number in range(n):
        for elem in lst:
            combination = elem + str(number)
            combinations.append(combination)
            # print(combination)
            # print('-' * 80)

    return combinations

print(concaten_func(the_list, cycles))
