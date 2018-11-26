# 25. Write a Python program to select an item randomly from a list.
import random

the_list = [2,'m', '90', 90, '$%^&', 'mmm', 1]

# random.shuffle(the_list)
# print(the_list[0])

random_index = random.randint(0, len(the_list) - 1)
print(the_list[random_index])

# print(random.choice(the_list))








